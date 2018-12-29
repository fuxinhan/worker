from datetime import datetime, timedelta
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    """ 用户 """
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名", help_text="姓名")
    birthday = models.DateField(null=True, blank=True, verbose_name="出生年月", help_text="出生年月")
    gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", "女")), default="female",
                              verbose_name="性别", help_text="性别")
    mobile = models.CharField(null=True, blank=True, max_length=100, verbose_name="手机号", help_text="手机号")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="邮箱", help_text="邮箱")
    address = models.CharField(max_length=100, null=True, blank=True, verbose_name="地址", help_text="地址")
    image = models.ImageField(upload_to="image/%Y/%m", null=True, blank=True, verbose_name="头像", help_text="头像")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    """ 邮箱验证码 """
    code = models.CharField(max_length=20, verbose_name="邮箱验证码", help_text="邮箱验证码")
    email = models.EmailField(max_length=50, verbose_name="邮箱", help_text="邮箱")
    # send_type = models.CharField(max_length=30, verbose_name="验证码类型", help_text="验证码类型",
    #                              choices=(("register", "注册"), ("forget", "找回密码"), ("update_emial", "修改邮箱")))
    send_time = models.DateTimeField(default=datetime.now, verbose_name="发送时间")

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code


class VerifyCode(models.Model):
    """ 短信验证码 """
    code = models.CharField(max_length=10, verbose_name="短信验证码", help_text="短信验证码")
    mobile = models.CharField(max_length=11, verbose_name="手机号", help_text="手机号")
    send_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text="添加时间")

    class Meta:
        verbose_name = "短信验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code
