from datetime import datetime

from django.db import models
from DjangoUeditor.models import UEditorField


class CityDict(models.Model):
    """ 城市信息 """
    name = models.CharField(max_length=100, verbose_name="城市", help_text="城市")
    desc = models.CharField(max_length=200, verbose_name="描述", help_text="描述")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text="添加时间")

    class Meta:
        verbose_name = u"城市"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseOrg(models.Model):
    """ 课程机构基本信息 """
    CATEGORY_CHOICES = (
        (1, "培训机构"),
        (2, "个人"),
        (3, "中小学"),
        (4, "大学"),
    )
    name = models.CharField(max_length=50, verbose_name="机构名称", help_text="机构名称")
    detail = UEditorField(verbose_name="机构描述", imagePath="org/images/", width=1000, height=300,
                          filePath="org/files/", default='', help_text="机构描述")
    category = models.IntegerField(default=1, verbose_name="机构类别", help_text="机构类别", choices=CATEGORY_CHOICES)
    click_nums = models.IntegerField(default=0, verbose_name="点击数", help_text="点击数")
    fav_num = models.IntegerField(default=0, verbose_name="收藏数", help_text="收藏数")
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name="封面图", help_text="封面图")
    address = models.CharField(max_length=150, verbose_name="机构地址", help_text="机构地址")
    city = models.ForeignKey(CityDict, on_delete=models.CASCADE, verbose_name="所在城市", help_text="所在城市")
    students = models.IntegerField(default=0, verbose_name="学习人数", help_text="学习人数")
    course_nums = models.IntegerField(default=0, verbose_name="课程数", help_text="课程数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text="添加时间")

    class Meta:
        verbose_name = "课程机构"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Teacher(models.Model):
    """ 教师基本信息 """
    org = models.ForeignKey(CourseOrg, on_delete=models.CASCADE,verbose_name="所属机构", help_text="所属机构")
    name = models.CharField(max_length=50, verbose_name="教师名", help_text="教师名")
    work_years = models.IntegerField(default=0, verbose_name="工作年限", help_text="工作年限")
    work_company = models.CharField(max_length=50, null=True, blank=True, verbose_name="就职公司", help_text="就职公司")
    work_position = models.CharField(max_length=50, null=True, blank=True, verbose_name="公司职位", help_text="公司职位")
    points = models.CharField(max_length=50, null=True, blank=True, verbose_name="教学特点", help_text="教学特点")
    click_nums = models.IntegerField(default=0, verbose_name="点击数", help_text="点击数")
    fav_num = models.IntegerField(default=0, verbose_name="收藏数", help_text="收藏数")
    age = models.IntegerField(default=18, verbose_name="年龄", help_text="年龄")
    image = models.ImageField(default='', upload_to="teacher/%Y/%m", verbose_name="头像", max_length=100, help_text="头像")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text="添加时间")

    class Meta:
        verbose_name = "教师"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
