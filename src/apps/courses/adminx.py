# -*- coding: utf-8 -*-
import xadmin
from .models import Course, Lesson, Video, CourseResource, LessonContent


class CourseAdmin(object):
    list_display = ['name', 'market_price', 'shop_price', 'degree', 'learn_times', 'students', 'fav_nums', 'click_nums', 'sold_num']
    search_fields = ['name', 'is_new', 'is_hot', 'goods_sn', 'market_price', 'shop_price', 'desc', 'detail', 'degree', 'students', 'fav_nums', 'click_nums']
    list_filter = ['name', 'is_new', 'is_hot', 'goods_sn', 'market_price', 'shop_price', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'click_nums', 'add_time']
    style_fields = {"detail": "ueditor"}


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']


class LessonContentAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course__name', 'name', 'download', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(LessonContent, LessonContentAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
