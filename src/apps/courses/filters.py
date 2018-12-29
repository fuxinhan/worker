import django_filters
from django.db.models import Q

from .models import Course


class CourseFilter(django_filters.rest_framework.FilterSet):
    """ 课程的过滤 """
    pricemin = django_filters.NumberFilter(field_name="shop_price", lookup_expr="gte", help_text="最低价格")
    pricemax = django_filters.NumberFilter(field_name="shop_price", lookup_expr="lte", help_text="最高价格")
    top_category = django_filters.NumberFilter(method='top_category_filter')

    # 找到某一类商品的所有数据
    def top_category_filter(self, queryset, name, value):
        return queryset.filter(Q(degree=value))

    class Meta:
        model = Course
        fields = ['pricemin', 'pricemax', 'is_hot', 'is_new']
