from datetime import datetime

from django.db import models
from DjangoUeditor.models import UEditorField
from django.contrib.auth import get_user_model

User = get_user_model()


class Sketch(models.Model):
    """ 作品信息 """
    CATEGORY_CHOICES = (
        (0, "显示官网展示"),
        (1, "不显示在官网"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户", help_text="用户")
    code_show = models.IntegerField(default=1, verbose_name="作品是否展示", help_text="作品是否展示", choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=20, verbose_name="作品名", help_text="作品名")
    desc = models.CharField(default='', max_length=200, verbose_name="描述", help_text="描述")
    detail = UEditorField(verbose_name="作品详情", imagePath="sketch/images/", width=1000, height=300,
                          filePath="sketch/files/", default='', help_text="作品详情")
    xml_send_data = models.TextField(default='', verbose_name="XmlSendData", help_text="XML数据流")  # XmlSendData 变量保存
    image_data = models.TextField(default='', verbose_name="iamgeData", help_text="图片数据流")
    content = models.TextField(default='', verbose_name="codeData", help_text="代码数据流")
    xml_title = models.CharField(default='', max_length=300, verbose_name="xml标题", help_text="xml标题")
    image = models.ImageField(default='', upload_to="sketch/images/%Y/%m", verbose_name="作品缩略图", help_text="作品缩略图")
    sketch = models.FileField(upload_to="sketch/%Y/%m", verbose_name="作品", default="", help_text="作品")
    url = models.CharField(max_length=200, verbose_name="作品地址", default="", help_text="作品地址")
    category = models.CharField(default="数字艺术", max_length=100, verbose_name="作品类别", help_text="作品类别")
    tag = models.CharField(default='', verbose_name="作品标签", max_length=300, help_text="作品标签")
    click_nums = models.IntegerField(default=0, verbose_name="点击数", help_text="点击数")
    fav_num = models.IntegerField(default=0, verbose_name="收藏数", help_text="收藏数")
    fork_num = models.IntegerField(default=0, verbose_name="再创作数", help_text="再创作数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text="添加时间")

    class Meta:
        ordering = ['-id']
        verbose_name = "作品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
