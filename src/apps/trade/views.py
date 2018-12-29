from django.shortcuts import redirect
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication

from lib.permissions import IsOwnerOrReadOnly
from .serializers import ShopCartSerializer, ShopCartDetailSerializer, OrderSerializer, OrderDetailSerializer
from .models import ShoppingCart, OrderInfo, OrderGoods


class ShoppingCartViewSet(viewsets.ModelViewSet):
    """
    购物车功能
    list:
        获取购物车详情
    create:
        加入购物车
    delete:
        删除购物记录
    update:
        更新购物商品数量
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = ShopCartSerializer
    # queryset = ShoppingCart.objects.all()
    lookup_field = "course_id"

    # def perform_create(self, serializer):
    #     shop_cart = serializer.save()
    #     goods = shop_cart.goods
    #     goods.goods_num -= shop_cart.goods_num
    #     goods.save()
    #
    # def perform_destroy(self, instance):
    #     goods = instance.goods
    #     goods.goods_num += instance.nums
    #     goods.save()
    #     instance.delete()
    #
    # def perform_update(self, serializer):
    #     existed_record = ShoppingCart.objects.get(id=serializer.instance.id)
    #     existed_nums = existed_record.nums
    #     saved_record = serializer.save()
    #     nums = saved_record.nums - existed_nums
    #     goods = saved_record.goods
    #     goods.goods_num -= nums
    #     goods.save()
    #
    def get_serializer_class(self):
        if self.action == 'list':
            return ShopCartDetailSerializer
        else:
            return ShopCartSerializer

    def get_queryset(self):
        return ShoppingCart.objects.filter(user=self.request.user)


class OrderViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    """
    订单管理
    list:
        获取个人订单
    delete:
        删除订单
    create:
        新增订单
    retrieve:
        订单详情
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = OrderSerializer

    def get_queryset(self):
        return OrderInfo.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return OrderDetailSerializer
        return OrderSerializer

    def perform_create(self, serializer):
        order = serializer.save()
        shop_carts = ShoppingCart.objects.filter(user=self.request.user)
        for shop_cart in shop_carts:
            order_goods = OrderGoods()
            order_goods.courser = shop_cart.course
            order_goods.goods_num = shop_cart.nums
            order_goods.order = order
            order_goods.save()

            shop_cart.delete()
        return order


from rest_framework.views import APIView
from lib.alipay import AliPay
from djangoreactredux.settings.base import ali_pub_key_path, private_key_path, appid, return_url
from datetime import datetime, timedelta
from rest_framework.response import Response


class AliPayView(APIView):
    def get(self, request):
        """ 处理支付宝 return_url 返回"""
        processed_dict = {}
        # 1. 获取GET中的参数
        for key, value in request.GET.items():
            processed_dict[key] = value
        # 2. 取出sign
        sign = processed_dict.pop("sign", None)

        # 3. 生成ALipay对象
        alipay = AliPay(
            appid=appid,
            app_notify_url=return_url,
            app_private_key_path=private_key_path,  # 个人私钥
            alipay_public_key_path=ali_pub_key_path,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            debug=True,  # 默认False,
            return_url=return_url
        )

        verify_result = alipay.verify(processed_dict, sign)
        if verify_result is True:
            # order_sn = processed_dict.get("out_trade_no", None)
            # trade_no = processed_dict.get("trade_no", None)
            # trade_status = processed_dict.get("trade_status", None)
            #
            # existed_orders = OrderInfo.objects.filter(order_sn=order_sn)
            #
            # for existed_order in existed_orders:
            #     existed_order.pay_status = trade_status
            #     existed_order.trade_no = trade_no
            #     existed_order.pay_time = datetime.now()
            #     existed_order.expire_time = datetime.now() + timedelta(days=30)
            #     # existed_order.deadline.expired_time = datetime.now() + timedelta(days=60)
            #     existed_order.save()

            # return Response("success")
            # response = redirect("index")
            response = redirect("/pay/introIndex/5/#/")
            # response.set_cookie("nextPath", "pay", max_age=2)
            return response
        else:
            response = redirect("login")
            return response

    def post(self, request):
        """ 处理支付宝 notify_url """
        # 1. 先将sign剔除掉
        processed_dict = {}
        for key, value in request.POST.items():
            processed_dict[key] = value

        sign = processed_dict.pop("sign", None)

        # 2. 生成一个Alipay对象
        alipay = AliPay(
            appid=appid,
            app_notify_url=return_url,
            app_private_key_path=private_key_path,  # 个人私钥
            alipay_public_key_path=ali_pub_key_path,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            debug=True,  # 默认False,
            return_url=return_url
        )

        # 3. 进行验签，确保这是支付宝给我们的
        verify_result = alipay.verify(processed_dict, sign)

        # 4. 如果验签成功
        if verify_result is True:
            order_sn = processed_dict.get("out_trade_no", None)
            trade_no = processed_dict.get("trade_no", None)
            trade_status = processed_dict.get("trade_status", None)

            # 查询数据库中存在的订单
            existed_orders = OrderInfo.objects.filter(order_sn=order_sn)
            for existed_order in existed_orders:
                # 订单商品项
                order_goods = existed_order.goods.all()  #order_info是order_goods的外键，通过related_name反向取order_goods
                # 商品销量增加订单中的数值
                for order_good in order_goods:
                    goods = order_good.courser
                    goods.sold_num += order_good.goods_num
                    goods.save()

                # 更新订单状态，填充支付宝给的交易凭证号
                existed_order.pay_status = trade_status
                existed_order.trade_no = trade_no
                existed_order.pay_time = datetime.now()
                existed_order.expire_time = datetime.now() + timedelta(days=30)
                # existed_order.deadline.expired_time = datetime.now() + timedelta(days=60)
                existed_order.save()

            # 将success返回给支付宝，支付宝就不会一直不停的继续发消息等待支付成功了
            return Response("success")
