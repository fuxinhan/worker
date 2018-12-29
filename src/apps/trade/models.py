from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

from courses.models import Course
from user_operation.models import UserDeadline

User = get_user_model()


class ShoppingCart(models.Model):
    """ 购物车 """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户", help_text="用户")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="购买课程", help_text="购买课程")
    nums = models.IntegerField(default=1, verbose_name="购买数量", help_text="购买数量")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text="添加时间")

    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = verbose_name
        unique_together = ("user", "course")

    def __str__(self):
        return "%s(%d)".format(self.course.name, self.nums)


class OrderInfo(models.Model):
    """ 订单基本信息 """
    ORDER_STATUS = (
        ("TRADE_SUCCESS", "交易支付成功"),
        ("TRADE_CLOSED", "未付款交易超时关闭，或支付完成后全额退款"),
        ("WAIT_BUYER_PAY", "交易创建，等待买家付款"),
        ("TRADE_FINISHED", "交易结束，不可退款"),
        ("paying", "待支付"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户", help_text="")
    order_sn = models.CharField(max_length=30, null=True, blank=True, unique=True, verbose_name="订单号", help_text="订单号")
    trade_no = models.CharField(max_length=100, unique=True, null=True, blank=True, verbose_name="交易号", help_text="交易号")
    pay_status = models.CharField(choices=ORDER_STATUS, default="paying", max_length=30, verbose_name="订单状态", help_text="订单状态")
    post_script = models.CharField(max_length=200, null=True, blank=True, verbose_name="订单留言", help_text="订单留言")
    order_mount = models.FloatField(default=0.0, verbose_name="订单金额", help_text="订单金额")
    pay_time = models.DateTimeField(null=True, blank=True, verbose_name="支付时间", help_text="支付时间")
    expire_time = models.DateTimeField(null=True, blank=True, verbose_name="过期时间", help_text="过期时间")
    deadline = models.ForeignKey(UserDeadline, on_delete=models.CASCADE, null=True, blank=True, verbose_name="使用截止时间", help_text="使用截止时间")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text="添加时间")

    class Meta:
        verbose_name = "订单"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order_sn)


class OrderGoods(models.Model):
    """ 订单的课程详情 """
    order = models.ForeignKey(OrderInfo, on_delete=models.CASCADE, verbose_name="订单信息", related_name="goods", help_text="订单信息")
    courser = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="商品", help_text="商品")
    goods_num = models.IntegerField(default=0, verbose_name="商品数量", help_text="商品数量")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text="添加时间")

    class Meta:
        verbose_name = "订单课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order.order_sn)
