import time
from rest_framework import serializers

from courses.models import Course
from .models import ShoppingCart, OrderInfo, OrderGoods
from courses.serializers import CourseSerializer
from lib.alipay import AliPay
from djangoreactredux.settings.base import private_key_path, ali_pub_key_path, appid, return_url
from user_operation.serializers import UserDeadlineSerializer
from user_operation.models import UserDeadline


class ShopCartDetailSerializer(serializers.ModelSerializer):
    course = CourseSerializer(many=False)

    class Meta:
        model = ShoppingCart
        fields = "__all__"


class ShopCartSerializer(serializers.Serializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    nums = serializers.IntegerField(required=True, min_value=1, max_value=3, error_messages={
                                             "min_value": "商品数量不能小于1",
                                             "max_value": "商品数量不能大于3",
                                             "required": "请选择购买数量",
                                         })
    course = serializers.PrimaryKeyRelatedField(required=True, queryset=Course.objects.all())

    def create(self, validated_data):
        user = self.context["request"].user
        nums = validated_data["nums"]
        course = validated_data["course"]

        existed = ShoppingCart.objects.filter(user=user, course=course)

        if existed:
            existed = existed[0]
            existed.nums += nums
            existed.save()
        else:
            existed = ShoppingCart.objects.create(**validated_data)

        return existed

    def update(self, instance, validated_data):
        # 修改商品数量
        instance.nums = validated_data["nums"]
        instance.save()
        return instance


class OrderGoodsSerializer(serializers.ModelSerializer):
    courser = CourseSerializer(many=False)

    class Meta:
        model = OrderGoods
        fields = "__all__"


class OrderDetailSerializer(serializers.ModelSerializer):
    # 一个订单有多个订单商品项
    deadline = UserDeadlineSerializer(many=False)
    goods = OrderGoodsSerializer(many=True)
    alipay_url = serializers.SerializerMethodField(read_only=True)

    def get_alipay_url(self, obj):
        alipay = AliPay(
            appid=appid,
            app_notify_url=return_url,
            app_private_key_path=private_key_path,  # 个人私钥
            alipay_public_key_path=ali_pub_key_path,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            debug=False,  # 默认False,
            return_url=return_url
        )
        url = alipay.direct_pay(
            subject=obj.order_sn,
            out_trade_no=obj.order_sn,
            total_amount=obj.order_mount,
        )
        re_url = "https://openapi.alipay.com/gateway.do?{data}".format(data=url)

        return re_url

    class Meta:
        model = OrderInfo
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    # deadline = serializers.PrimaryKeyRelatedField(many=False, read_only=True) 更新外键
    # deadline = UserDeadlineSerializer(many=False, read_only=True, required=False)

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    pay_status = serializers.CharField(read_only=True)
    trade_no = serializers.CharField(read_only=True)
    order_sn = serializers.CharField(read_only=True)
    pay_time = serializers.DateTimeField(read_only=True)
    expire_time = serializers.DateTimeField(read_only=True)

    # order_mount = serializers.FloatField(read_only=True)
    alipay_url = serializers.SerializerMethodField(read_only=True)

    def get_alipay_url(self, obj):
        alipay = AliPay(
            appid=appid,
            app_notify_url=return_url,
            app_private_key_path=private_key_path,  # 个人私钥
            alipay_public_key_path=ali_pub_key_path,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            debug=True,  # 默认False,
            return_url=return_url
        )
        url = alipay.direct_pay(
            subject=obj.order_sn,
            out_trade_no=obj.order_sn,
            total_amount=obj.order_mount,
        )
        re_url = "https://openapi.alipay.com/gateway.do?{data}".format(data=url)

        return re_url  # 序列化的时候生成支付宝的支付url

    def generate_order_sn(self):
        # 当前时间+userid+随机数
        from random import Random
        random_ins = Random()
        order_sn = "{time_str}{userid}{ranstr}".format(time_str=time.strftime("%Y%m%d%H%M%S"),
                                                       userid=self.context["request"].user.id,
                                                       ranstr=random_ins.randint(10, 99))
        return order_sn

    def validate(self, attrs):
        attrs["order_sn"] = self.generate_order_sn()
        return attrs

    class Meta:
        model = OrderInfo
        fields = "__all__"
