import django_filters

from .models import Sketch


class SketchFilter(django_filters.rest_framework.FilterSet):
    """ 课程的过滤 """
    minclick_nums = django_filters.NumberFilter(name="click_nums", lookup_expr="gte", help_text="最低点击数")
    maxclick_nums = django_filters.NumberFilter(name="click_nums", lookup_expr="lte", help_text="最高点击数")
    minfav_num = django_filters.NumberFilter(name="fav_num", lookup_expr="gte", help_text="最低收藏数")
    maxfav_num = django_filters.NumberFilter(name="fav_num", lookup_expr="lte", help_text="最高收藏数")
    minfork_num = django_filters.NumberFilter(name="fork_num", lookup_expr="gte", help_text="最低再创作数")
    maxfork_num = django_filters.NumberFilter(name="fork_num", lookup_expr="lte", help_text="最高再创作数")

    class Meta:
        model = Sketch
        fields = ['name', 'desc', 'xml_title', 'tag', 'minclick_nums', 'maxclick_nums', 'minfav_num', 'maxfav_num',
                  'minfork_num', 'maxfork_num', 'add_time']
