from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication

from .models import UserEnroll, SalesInfo, UserFavoriteCourse, UserCourse, UserFavoriteOrg, UserFavoriteSketch
from lib.permissions import IsOwnerOrReadOnly
from .serializers import UserEnrollDetailSerializer, UserEnrollSerializer, UserFavCourseSerializer, UserFavCourseDetailSerializer, UserSketchSerializer, \
    UserCourseSerializer, UserCourseDetailSerializer, SalesInfoDetailSerializer, SalesInfoSerializer, UserDeadlineSerializer
from sketch.models import Sketch


class UserEnrollViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    报名表管理
    list:
        获取用户报名列表
    retrieve:
        报名详情
    create：
        用户添加报名
    delete：
        删除用户报名
    """
    serializer_class = UserEnrollSerializer

    def get_queryset(self):
        return UserEnroll.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return UserEnrollDetailSerializer

        return UserEnrollSerializer


class SalesInfoViewSet(viewsets.ModelViewSet):
    """
    销售信息管理
    list:
        销售信息管理
    retrieve:
        销售信息详情
    create:
        新增销售信息
    delete:
        删除销售信息
    """
    serializer_class = SalesInfoSerializer
    queryset = SalesInfo.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return SalesInfoDetailSerializer

        return SalesInfoSerializer


class UserFavCourseViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                           mixins.DestroyModelMixin, viewsets.GenericViewSet):
    """
    list:
        获取用户收藏课程列表
    retrieve:
        判断某个商品是否已经收藏
    create:
        收藏商品
    destroy:
        取消收藏
    """
    # queryset = UserFav.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    # serializer_class = UserFavSerializer
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    lookup_field = "course_id"

    def get_queryset(self):
        return UserFavoriteCourse.objects.filter(user=self.request.user)

    # def perform_create(self, serializer):
    #     instance = serializer.save()
    #     goods = instance.goods
    #     goods.fav_num += 1
    #     goods.save()

    def get_serializer_class(self):
        if self.action == 'list':
            return UserFavCourseDetailSerializer
        elif self.action == 'create':
            return UserFavCourseSerializer
        elif self.action == 'retrieve':
            return UserFavCourseDetailSerializer

        return UserFavCourseSerializer


class UserSketchViewSet(viewsets.ModelViewSet):
    """
    用户个人作品展示
        list:
            获取用户作品列表
        create:
            新增作品
        delete:
            删除作品
        update:
            更新作品
        retieve:
            获取作品详情
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = UserSketchSerializer

    # queryset = Sketch.objects.all()

    def get_queryset(self):
        return Sketch.objects.filter(user=self.request.user)


class UserCourseViewSet(viewsets.ModelViewSet):
    """
    用户购买的课程
        list:
            获取用户已购买的课程
        create:
            新增课程
        retrieve:
            获取课程详情
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    # serializer_class = UserCourseSerializer

    # queryset = UserCourse.objects.all()
    def get_serializer_class(self):
        if self.action == 'list':
            return UserCourseDetailSerializer
        if self.action == 'retrieve':
            return UserCourseDetailSerializer
        else:
            return UserCourseSerializer

    def get_queryset(self):
        return UserCourse.objects.filter(user=self.request.user)


class UserDeadlineViewSet(viewsets.ModelViewSet):
    """
    用户使用期限
        list：获取用户使用的期限
        create：新增用户使用的期限
        retrieve：获取用户使用期限的详情
        delete：删除用户使用期限
        update：更新用户使用期限
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = UserDeadlineSerializer

    def get_queryset(self):
        return UserCourse.objects.filter(user=self.request.user)
