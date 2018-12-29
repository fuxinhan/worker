import re
from datetime import datetime, timedelta
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.core.validators import validate_email
from rest_framework.validators import UniqueValidator

from djangoreactredux.settings.base import REGEX_MOBILE
from .models import VerifyCode, EmailVerifyRecord

User = get_user_model()


class SmsSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11, help_text="手机号")

    def validate_mobile(self, mobile):
        """ 验证手机号码  """
        # 手机是否注册
        if User.objects.filter(mobile=mobile).count():
            raise serializers.ValidationError("用户已经存在")
        # 验证手机号码是否合法
        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError("手机号码非法")
        # 验证发送频率
        one_mintes_ago = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        if VerifyCode.objects.filter(send_time__gt=one_mintes_ago, mobile=mobile).count():
            raise serializers.ValidationError("距离上次发送未超过60秒")

        return mobile


class SmsSerializer1(serializers.Serializer):
    mobile = serializers.CharField(max_length=11, help_text="手机号")

    def validate_mobile(self, mobile):
        """ 验证手机号码  """
        # 手机是否注册
        if not User.objects.filter(mobile=mobile).count():
            raise serializers.ValidationError("用户不存在")
        # 验证手机号码是否合法
        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError("手机号码非法")
        # 验证发送频率
        one_mintes_ago = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        if VerifyCode.objects.filter(send_time__gt=one_mintes_ago, mobile=mobile).count():
            raise serializers.ValidationError("距离上次发送未超过60秒")

        return mobile


class ChangSmsSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11, help_text="手机号")

    def validate_mobile(self, mobile):
        """ 验证手机号码  """
        # 手机是否注册
        if not User.objects.filter(mobile=mobile).count():
            raise serializers.ValidationError("用户不存在")
        # 验证手机号码是否合法
        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError("手机号码非法")
        # 验证发送频率
        one_mintes_ago = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        if VerifyCode.objects.filter(send_time__gt=one_mintes_ago, mobile=mobile).count():
            raise serializers.ValidationError("距离上次发送未超过60秒")

        return mobile


class EmailSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=50, help_text="邮箱地址")

    def validate_email(self, email):
        """ 验证邮箱地址 """
        # 邮箱是否注册
        if User.objects.filter(email=email).count():
            raise serializers.ValidationError("邮箱已经存在")
        # 验证邮箱是否合法
        validate_email(email)
        # 验证发送频率
        one_mintes_ago = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        if EmailVerifyRecord.objects.filter(send_time__gt=one_mintes_ago, email=email).count():
            raise serializers.ValidationError("距离上次发送未超过60秒")

        return email


class UserDetailSerializer(serializers.ModelSerializer):
    """ 用户详情序列化类 """

    class Meta:
        model = User
        fields = ("name", "gender", "birthday", "email", "mobile", "address", "username")


class UserRegSerializer(serializers.ModelSerializer):
    code = serializers.CharField(required=True, max_length=4, min_length=4,
                                 write_only=True,
                                 label="验证码",
                                 error_messages={
                                     "blank": "请输入验证码",
                                     "required": "请输入验证码",
                                     "max_length": "验证码格式错误",
                                     "min_length": "验证码格式错误",
                                 }, help_text="验证码")
    username = serializers.CharField(required=True, allow_blank=False, label="用户名", help_text="用户名",
                                     validators=[UniqueValidator(queryset=User.objects.all(),
                                                                 message="用户已经存在")])
    password = serializers.CharField(
        style={'input_type': 'password'}, label="密码", write_only=True, help_text="密码",
    )

    def validate_code(self, code):
        verify_sms_records = VerifyCode.objects.filter(mobile=self.initial_data["username"]).order_by("-send_time")
        verify_email_records = EmailVerifyRecord.objects.filter(email=self.initial_data["username"]).order_by(
            "-send_time")
        if verify_sms_records:
            verify_records = verify_sms_records
        else:
            verify_records = verify_email_records

        if verify_records:
            last_records = verify_records[0]  # 最近的一个验证码
            five_mintes_ago = datetime.now() - timedelta(hours=0, minutes=5, seconds=0)  # 有效期为5分钟
            if five_mintes_ago > last_records.send_time:
                raise serializers.ValidationError("验证码过期")
            if last_records.code != code:
                raise serializers.ValidationError("验证码错误")  # 验证码输入错误
        else:
            raise serializers.ValidationError("验证码错误")  # 记录都不存在

    def validate(self, attrs):
        attrs["mobile"] = attrs["username"]
        attrs["email"] = attrs["username"]
        del attrs["code"]
        return attrs

    class Meta:
        model = User
        fields = ("username", "code", "mobile", "email", "password")


class UserDetailSerializer(serializers.ModelSerializer):
    """ 用户详情序列化类 """

    class Meta:
        model = User
        fields = ("name", "gender", "birthday", "email", "mobile", "address", "username")


class UpdatePasswordSerializer(serializers.Serializer):
    """用户修改密码序列化"""
    code = serializers.CharField(required=True, max_length=4, min_length=4,
                                 write_only=True,
                                 label="验证码",
                                 error_messages={
                                     "blank": "请输入验证码",
                                     "required": "请输入验证码",
                                     "max_length": "验证码格式错误",
                                     "min_length": "验证码格式错误",
                                 }, help_text="验证码")
    password = serializers.CharField(
        style={'input_type': 'password'}, label="密码", write_only=True, help_text="密码",
    )

    def validate_code(self, code):
        verify_sms_records = VerifyCode.objects.filter(mobile=self.initial_data["username"]).order_by("-send_time")
        verify_email_records = EmailVerifyRecord.objects.filter(email=self.initial_data["username"]).order_by(
            "-send_time")
        if verify_sms_records:
            verify_records = verify_sms_records
        else:
            verify_records = verify_email_records

        if verify_records:
            last_records = verify_records[0]  # 最近的一个验证码
            five_mintes_ago = datetime.now() - timedelta(hours=0, minutes=5, seconds=0)  # 有效期为5分钟
            if five_mintes_ago > last_records.send_time:
                raise serializers.ValidationError("验证码过期")
            if last_records.code != code:
                raise serializers.ValidationError("验证码错误")  # 验证码输入错误
        else:
            raise serializers.ValidationError("验证码错误")  # 记录都不存在

    def update(self, instance, validated_data):
        user = self.context["request"].user
        user.set_password(validated_data["password"])
        user.save()
        return user

    def validate(self, attrs):
        attrs["mobile"] = attrs["username"]
        attrs["email"] = attrs["username"]
        del attrs["code"]
        return attrs

    class Meta:
        model = User
        fields = ("password", "code")


"""
"password", "name", "gender", "birthday", "email", "mobile", "address", "username", "code"

"""