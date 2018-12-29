from random import choice

from django.core.mail import send_mail
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import viewsets, status, mixins, permissions, authentication
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler

from .serializers import SmsSerializer, EmailSerializer, UserRegSerializer, UserDetailSerializer, \
    UpdatePasswordSerializer, ChangSmsSerializer, SmsSerializer1
from lib.yunpian import YunPian
from djangoreactredux.settings.base import APIKEY, EMAIL_FROM
from .models import VerifyCode, EmailVerifyRecord

User = get_user_model()


class CustomBackend(ModelBackend):
    """ 自定义用户验证 """

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(email=username) | Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class SmsCodeViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """ 发送短信验证码 """
    serializer_class = SmsSerializer

    def generate_code(self):
        """ 生成四位数字的验证码 """
        seeds = "1234567890"
        random_str = []
        for i in range(4):
            random_str.append(choice(seeds))

        return "".join(random_str)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        mobile = serializer.validated_data["mobile"]
        yun_pian = YunPian(APIKEY)
        code = self.generate_code()
        sms_status = yun_pian.send_sms(code=code, mobile=mobile)
        if sms_status["code"] != 0:
            return Response({
                "mobile": sms_status["msg"]
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            code_record = VerifyCode(code=code, mobile=mobile)
            code_record.save()
            return Response({
                "mobile": mobile
            }, status=status.HTTP_201_CREATED)
class SmsCodeViewSet1(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """ 发送短信验证码 """
    serializer_class = SmsSerializer1

    def generate_code(self):
        """ 生成四位数字的验证码 """
        seeds = "1234567890"
        random_str = []
        for i in range(4):
            random_str.append(choice(seeds))

        return "".join(random_str)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        mobile = serializer.validated_data["mobile"]
        yun_pian = YunPian(APIKEY)
        code = self.generate_code()
        sms_status = yun_pian.send_sms(code=code, mobile=mobile)
        if sms_status["code"] != 0:
            return Response({
                "mobile": sms_status["msg"]
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            code_record = VerifyCode(code=code, mobile=mobile)
            code_record.save()
            return Response({
                "mobile": mobile
            }, status=status.HTTP_201_CREATED)

class EmailCodeViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """ 发送邮箱验证码 """
    serializer_class = EmailSerializer

    def generate_code(self):
        """ 生成四位数字的验证码 """
        seeds = "1234567890"
        random_str = []
        for i in range(4):
            random_str.append(choice(seeds))

        return "".join(random_str)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]
        code = self.generate_code()
        email_title = "YaK芽课 验证码"
        email_body = "您的邮箱验证码为：{0}".format(code)
        email_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if email_status == 1:
            code_record = EmailVerifyRecord(code=code, email=email)
            code_record.save()
            return Response({
                "email": email
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "mobile": email_status["msg"]
            }, status=status.HTTP_400_BAD_REQUEST)
"""
mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
"""

class UserViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet ):
    """ 用户 """
    serializer_class = UserRegSerializer
    queryset = User.objects.all()
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
    # def list(self,request,*args,**kwargs):
    #     print(request.user)
    #     super(UserViewSet, self).list(request,*args,**kwargs)
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return UserDetailSerializer
        elif self.action == 'create':
            return UserRegSerializer
        elif self.action == "update":
            return UpdatePasswordSerializer
        return UserDetailSerializer

    # permission_classes = (permissions.IsAuthenticated, )
    def get_permissions(self):
        if self.action == 'retrieve':
            return [permissions.IsAuthenticated()]
        elif self.action == 'update':
            return [permissions.IsAuthenticated()]
        elif self.action == 'create':
            return []

        return []  # 返回默认值为空一定要加，否则会出错的

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict["token"] = jwt_encode_handler(payload)
        re_dict["name"] = user.name if user.name else user.username

        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def get_object(self):
        return self.request.user

    def perform_update(self, serializer):
        serializer.save()


    def perform_create(self, serializer):
        return serializer.save()


