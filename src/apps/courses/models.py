from datetime import datetime

from django.db import models
from DjangoUeditor.models import UEditorField


class Course(models.Model):
    """ 课程基本信息 """
    DEGREE_TYPE = (
        (1, "1年级"),
        (2, "2年级"),
        (3, "3年级"),
        (4, "4年级"),
        (5, "5年级"),
        (6, "6年级"),
        (7, "初一"),
        (8, "初二"),
        (9, "初三"),
        (10, "高一"),
        (11, "高二"),
        (12, "高三"),
        (13, "大一"),
        (14, "大二"),
        (15, "大三"),
        (16, "大四"),
        (17, "成人"),
    )

    name = models.CharField(verbose_name="课程名", max_length=50, help_text="课程名")
    desc = models.CharField(verbose_name="课程简短描述", max_length=300, help_text="课程简短描述")
    detail = UEditorField(verbose_name="课程详情", imagePath="courses/images/", width=1000, height=300,
                          filePath="courses/files/", default='', help_text="课程详情")

    url = models.CharField(verbose_name="课程介绍视频地址", max_length=200, default="", help_text="课程介绍视频地址")
    degree = models.IntegerField(verbose_name="难度", choices=DEGREE_TYPE, default=3, help_text="难度")
    learn_times = models.IntegerField(verbose_name="学习时长(分钟)", default=0, help_text="学习时长(分钟)")
    students = models.IntegerField(verbose_name="学习人数", default=0, help_text="学习人数")
    fav_nums = models.IntegerField(verbose_name="收藏人数", default=0, help_text="收藏人数")
    image = models.ImageField(verbose_name="封面图", upload_to="courses/%Y/%m", max_length=100, help_text="封面图")
    click_nums = models.IntegerField(verbose_name="点击数", default=0, help_text="点击数")
    category = models.CharField(verbose_name="课程类别", default="数字艺术", max_length=20, help_text="课程类别")
    tag = models.CharField(verbose_name="课程标签", default='', max_length=10, help_text="课程标签")
    youneed_know = models.CharField(verbose_name="课程须知", default='', max_length=300, help_text="课程须知")
    teacher_tell = models.CharField(verbose_name="能学到什么", default='', max_length=300, help_text="能学到什么")
    sold_num = models.IntegerField(default=0, verbose_name="课程销量", help_text="已付款人数")
    goods_sn = models.CharField(max_length=50, default="", verbose_name="课程商品唯一货号", help_text="商品唯一货号")
    market_price = models.FloatField(default=0, verbose_name="市场价格", help_text="原价")
    shop_price = models.FloatField(default=0, verbose_name="促销价", help_text="促销价")
    is_new = models.BooleanField(default=False, verbose_name="是否新品", help_text="是否新品")
    is_hot = models.BooleanField(default=False, verbose_name="是否热销", help_text="是否热销")
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now, help_text="添加时间")

    class Meta:
        ordering = ['-id']
        verbose_name = "课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Lesson(models.Model):
    """ 课程和章节之间一对多的关系 - 章节表  """
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程", help_text="课程", related_name="course")
    name = models.CharField(verbose_name="章节名", max_length=100, help_text="章节名")
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now, help_text="添加时间")

    class Meta:
        verbose_name = "章节"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Video(models.Model):
    """ 章节和视频之间一对多的关系 - 章节视频表 """
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name="章节", help_text="章节")
    name = models.CharField(max_length=100, verbose_name="视频名", help_text="视频名")
    url = models.CharField(max_length=200, verbose_name="章节视频访问地址", default="", help_text="章节视频访问地址")
    learn_times = models.IntegerField(default=0, verbose_name="学习时长(分钟)", help_text="学习时长(分钟)")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text="添加时间")

    class Meta:
        verbose_name = "章节视频"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class LessonContent(models.Model):
    """ 章节和内容之间一对多的关系 - 章节内容表 """
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name="章节", help_text="章节")
    name = models.CharField(max_length=100, verbose_name="章节内容名称", help_text="章节内容名称")
    url = models.CharField(max_length=200, verbose_name="章节内容访问地址", default="", help_text="章节内容访问地址")
    learn_times = models.IntegerField(default=0, verbose_name="学习时长(分钟)", help_text="学习时长(分钟)")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text="添加时间")

    class Meta:
        verbose_name = "章节内容"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResource(models.Model):
    """ 课程和资源之间一对多的关系 - 课程资源表 """
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程", help_text="课程")
    name = models.CharField(max_length=100, verbose_name="资源名称", help_text="资源名称")
    download = models.FileField(upload_to="courses/resource/%Y/%m", verbose_name="资源文件", max_length=100, help_text="资源文件")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text="添加时间")

    class Meta:
        ordering = ['-id']
        verbose_name = "课程资源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
