import xadmin
# from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from django.conf.urls import include, url
from django.views.decorators.cache import cache_page
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter

from djangoreactredux.settings.base import MEDIA_ROOT
from base import views as base_views
from users.views import SmsCodeViewSet, EmailCodeViewSet, UserViewSet, SmsCodeViewSet1
from courses.views import CourseListViewSet, LessonViewSet, LessonContentViewSet, VideoViewSet, CourseResourceViewSet
from trade.views import ShoppingCartViewSet, OrderViewSet, AliPayView
from user_operation.views import UserEnrollViewSet, SalesInfoViewSet, UserFavCourseViewSet, UserSketchViewSet, \
    UserSketchViewSet, UserCourseViewSet, UserDeadlineViewSet
from sketch.views import SketchListViewSet
from django.contrib import auth
from rest_framework_jwt import views

xadmin.autodiscover()
router = DefaultRouter()
router.register(r'smscodes', SmsCodeViewSet, base_name="smscodes")
router.register(r"smscode",SmsCodeViewSet1,base_name="smscode")
router.register(r'emailcodes', EmailCodeViewSet, base_name="emailcodes")
router.register(r'users', UserViewSet, base_name="users")
router.register(r'courses', CourseListViewSet, base_name="courses")
router.register(r'lesson', LessonViewSet, base_name="lesson")
router.register(r'lessoncontent', LessonContentViewSet, base_name="lessoncontent")
router.register(r'video', VideoViewSet, base_name="video")
router.register(r'courseres', CourseResourceViewSet, base_name="courseres")
router.register(r'shopcarts', ShoppingCartViewSet, base_name="shopcarts")
router.register(r'orders', OrderViewSet, base_name="orders")
router.register(r'userfavcourse', UserFavCourseViewSet, base_name="userfavcourse")
router.register(r'usersketch', UserSketchViewSet, base_name="usersketch")
router.register(r'sketch', SketchListViewSet, base_name="sketch")
router.register(r'usercourse', UserCourseViewSet, base_name="usercourse")
router.register(r'userenroll', UserEnrollViewSet, base_name="userenroll")
router.register(r'salesinfo', SalesInfoViewSet, base_name="salesinfo")
router.register(r'userdeadline', UserDeadlineViewSet, base_name="userdeadline")

urlpatterns = [
    url(r'^new-login/', auth.login, name="new-login"),
    url(r'^api/', include(router.urls), name="api"),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^tracking/', include('tracking.urls')),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'ueditor/', include('DjangoUeditor.urls')),
    url(r'docs/', include_docs_urls(title="文档功能")),
    url(r'^login/$', obtain_jwt_token, name="login"),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^alipay/return/', AliPayView.as_view(), name="alipay"),

    # url(r'^api/v1/accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^api/v1/getdata/', include('base.urls')),

    # catch all others because of how history is handled by react router - cache this page because it will never change
    url(r'^', cache_page(settings.PAGE_CACHE_SECONDS)(base_views.IndexView.as_view()), name='index'),


]
