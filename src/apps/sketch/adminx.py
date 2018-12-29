import xadmin
from .models import Sketch


class SketchAdmin(object):
    list_display = ['user', 'name', 'desc', 'url', 'click_nums', 'code_show', 'fav_num', 'fork_num', 'add_time']
    search_fields = ['user', 'name', 'desc', 'url', 'tag', 'click_nums', 'code_show', 'fav_num', 'fork_num', ]
    list_filter = ['user', 'name', 'desc', 'url', 'tag', 'click_nums', 'code_show', 'fav_num', 'fork_num', 'add_time']
    style_fields = {"detail": "ueditor"}


xadmin.site.register(Sketch, SketchAdmin)
