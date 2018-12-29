from rest_framework import mixins, generics, viewsets, filters, authentication
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Course, Lesson, LessonContent, CourseResource, Video
from .filters import CourseFilter
from .serializers import CourseSerializer, LessonSerializer, LessonContentSerializer, VideoSerializer, CourseResourceSerializer


class CourseListViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """ 课程列表页、详情、分页、搜索、过滤、排序"""
    throttle_classes = (UserRateThrottle, AnonRateThrottle)
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = CourseFilter
    search_fields = ('name', 'desc', 'degree', 'category', 'tag', 'youneed_know', 'teacher_tell')

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.click_nums += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class LessonViewSet(CacheResponseMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """ 课程章节列表页 """
    throttle_classes = (UserRateThrottle, AnonRateThrottle)
    queryset = Lesson.objects.all().order_by('id')
    serializer_class = LessonSerializer


class LessonContentViewSet(CacheResponseMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """ 课程章节内容列表页 """
    throttle_classes = (UserRateThrottle, AnonRateThrottle)
    queryset = LessonContent.objects.all().order_by('id')
    serializer_class = LessonContentSerializer
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)


class CourseResourceViewSet(CacheResponseMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """ 课程资源列表页 """
    throttle_classes = (UserRateThrottle, AnonRateThrottle)
    queryset = CourseResource.objects.all()
    serializer_class = CourseResourceSerializer
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)


class VideoViewSet(CacheResponseMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """ 课程章节视频列表页 """
    throttle_classes = (UserRateThrottle, AnonRateThrottle)
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
