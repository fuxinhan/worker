import xadmin
from .models import UserAsk, CourseComments, SketchComments, UserFavoriteCourse, UserFavoriteOrg, UserFavoriteSketch, \
    UserMessage, UserCourse, UserEnroll, SalesInfo, UserDeadline


class UserAskAdmin(object):
    list_display = ['name', 'mobile', 'course_name', 'desc', 'add_time']
    search_fields = ['name', 'mobile', 'course_name', 'desc']
    list_filter = ['name', 'mobile', 'course_name', 'desc', 'add_time']


class UserEnrollAdmin(object):
    list_display = ['name', 'birthday', 'gender', 'mobile', 'address', 'school', 'enroll', 'msg_ad', 'remark', 'add_time']
    search_fields = ['name', 'birthday', 'gender', 'mobile', 'address', 'school', 'enroll', 'msg_ad', 'remark']
    list_filter = ['name', 'birthday', 'gender', 'mobile', 'address', 'school', 'enroll', 'msg_ad', 'remark', 'add_time']


class SalesInfoAdmin(object):
    list_display = ['enroll_time', 'student', 'course', 'pay_mount', 'preferential_channels', 'know_yak', 'remark',
                    'add_time']
    search_fields = ['enroll_time', 'student', 'course', 'pay_mount', 'preferential_channels', 'know_yak', 'remark']
    list_filter = ['enroll_time', 'student', 'course', 'pay_mount', 'preferential_channels', 'know_yak', 'remark', 'add_time']


class CourseCommentsAdmin(object):
    list_display = ['user', 'course', 'comments', 'add_time']
    search_fields = ['user', 'course', 'comments']
    list_filter = ['user', 'course', 'comments', 'add_time']


class SketchCommentsAdmin(object):
    list_display = ['user', 'sketch', 'comments', 'add_time']
    search_fields = ['user', 'sketch', 'comments']
    list_filter = ['user', 'sketch', 'comments', 'add_time']


class UserFavoriteCourseAdmin(object):
    list_display = ['user', 'course', 'add_time']
    search_fields = ['user', 'course']
    list_filter = ['user', 'course', 'add_time']


class UserFavoriteOrgAdmin(object):
    list_display = ['user', 'org', 'add_time']
    search_fields = ['user', 'org']
    list_filter = ['user', 'org', 'add_time']


class UserFavoriteSketchAdmin(object):
    list_display = ['user', 'sketch', 'add_time']
    search_fields = ['user', 'sketch']
    list_filter = ['user', 'sketch', 'add_time']


class UserMessageAdmin(object):
    list_display = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message', 'has_read']
    list_filter = ['user', 'message', 'has_read', 'add_time']


class UserDeadlineAdmin(object):
    list_display = ['user', 'expired_time', 'add_time']
    search_fields = ['user', 'expired_time']
    list_filter = ['user', 'expired_time', 'add_time']


class UserCourseAdmin(object):
    list_display = ['user', 'course', 'add_time', 'deadline']
    search_fields = ['user', 'course', 'deadline']
    list_filter = ['user', 'course', 'add_time', 'deadline']


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(UserEnroll, UserEnrollAdmin)
xadmin.site.register(SalesInfo, SalesInfoAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
xadmin.site.register(SketchComments, SketchCommentsAdmin)
xadmin.site.register(UserFavoriteCourse, UserFavoriteCourseAdmin)
xadmin.site.register(UserFavoriteOrg, UserFavoriteOrgAdmin)
xadmin.site.register(UserFavoriteSketch, UserFavoriteSketchAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
xadmin.site.register(UserDeadline, UserDeadlineAdmin)
