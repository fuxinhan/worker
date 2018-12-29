from rest_framework import viewsets, mixins, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from .serializers import SketchSerializer, SketchDetailSerializer
from .models import Sketch
from .filters import SketchFilter


class SketchListViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
        所有作品展示
        list:
            获取所有作品列表
        retrieve:
            获取单个作品详情
        """
    throttle_classes = (UserRateThrottle, AnonRateThrottle)
    # queryset = Sketch.objects.all()
    # serializer_class = SketchSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = SketchFilter
    search_fields = ['name', 'desc', 'xml_title', 'tag', 'minclick_nums', 'maxclick_nums', 'minfav_num', 'maxfav_num',
                     'minfork_num', 'maxfork_num', 'add_time']

    def get_queryset(self):
        return Sketch.objects.filter(code_show__lt=1)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.click_nums += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == 'list':
            return SketchDetailSerializer
        else:
            return SketchSerializer
