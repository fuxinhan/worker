import xadmin
from xadmin import views
from .models import EmailVerifyRecord, VerifyCode


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_time']


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "YaK后台管理系统"
    site_footer = "上海牧学网络科技有限公司"
    menu_style = "accordion"


class VerifyCodeAdmin(object):
    list_display = ['code', 'mobile', "send_time"]
    search_fields = ['code', 'mobile']
    list_filter = ['code', 'mobile',  'send_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(VerifyCode, VerifyCodeAdmin)
