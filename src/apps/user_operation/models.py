from datetime import datetime, timedelta

from django.db import models
from django.contrib.auth import get_user_model

from courses.models import Course
from sketch.models import Sketch
from organization.models import CourseOrg, Teacher

User = get_user_model()


class UserAsk(models.Model):
    """ 用户咨询 """
    name = models.CharField(max_length=20, verbose_name="姓名", help_text="姓名")
    mobile = models.CharField(max_length=11, verbose_name="手机", help_text="手机")
    course_name = models.CharField(max_length=50, verbose_name="课程名", help_text="课程名")
    desc = models.CharField(max_length=200, verbose_name="描述", help_text="描述")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text="添加时间")

    class Meta:
        verbose_name = "用户咨询"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class UserEnroll(models.Model):
    """ 用户报名表 """
    name = models.CharField(max_length=20, verbose_name="学生姓名", help_text="学生姓名")
    birthday = models.DateField(null=True, blank=True, verbose_name="学生生日", help_text="学生生日")
    gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", "女")), default="female",
                              verbose_name="学生性别", help_text="学生性别")
    mobile = models.CharField(null=True, blank=True, max_length=100, verbose_name="家长手机号", help_text="家长手机号")
    address = models.CharField(null=True, blank=True, max_length=100, verbose_name="家庭住址", help_text="家庭住址")
    school = models.CharField(null=True, blank=True, max_length=100, verbose_name="入读学校", help_text="入读学校")
    enroll = models.CharField(null=True, blank=True, max_length=100, verbose_name="试听课时间选择", help_text="试听课时间选择")
    msg_ad = models.CharField(max_length=3, choices=(("yes", "是"), ("no", "否")), default="no",
                              verbose_name="是否愿意接受短信推广信息", help_text="是否愿意接受短信推广信息")
    remark = models.CharField(null=True, blank=True, max_length=200, verbose_name="备注", help_text="备注")
    add_time = models.DateField(default=datetime.now, verbose_name="添加时间", help_text="添加时间")

    class Meta:
        verbose_name = "微信及网页版报名信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class SalesInfo(models.Model):
    """ 销售信息 """
    enroll_time = models.DateField(verbose_name="报名时间", help_text="报名时间")
    student = models.ForeignKey(UserEnroll, on_delete=models.CASCADE, verbose_name="报名用户", help_text="报名用户")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="报名课程", help_text="报名课程")
    pay_mount = models.FloatField(default=0.0, verbose_name="实际付款", help_text="实际付款")
    preferential_channels = models.CharField(max_length=200, verbose_name="优惠渠道", help_text="优惠渠道")
    know_yak = models.CharField(max_length=200, verbose_name="如何了解YaK", help_text="如何了解YaK")
    remark = models.CharField(null=True, blank=True, max_length=200, verbose_name="备注", help_text="备注")
    add_time = models.DateField(default=datetime.now, verbose_name="添加时间", help_text="添加时间")

    class Meta:
        verbose_name = "销售信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.student.name


class CourseComments(models.Model):
    """ 课程评论 """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户", help_text="用户")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程", help_text="课程")
    comments = models.CharField(max_length=200, verbose_name="评论", help_text="评论")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text="添加时间")

    class Meta:
        verbose_name = "课程评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.comments


class SketchComments(models.Model):
    """ 作品评论 """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户", help_text="用户")
    sketch = models.ForeignKey(Sketch, on_delete=models.CASCADE, verbose_name="作品", help_text="作品")
    comments = models.CharField(max_length=200, verbose_name="留言", help_text="留言")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text="添加时间")

    class Meta:
        verbose_name = "作品评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.comments


class UserFavoriteCourse(models.Model):
    """ 用户收藏课程 """
    # FAV_TYPE = (
    #     (1, "课程"),
    #     (2, "课程机构"),
    #     (3, "讲师"),
    #     (4, "作品"),
    #     (5, "用户")
    # )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户", help_text="用户")
    # fav_id = models.IntegerField(default=0, verbose_name="收藏id", help_text="收藏id")
    # fav_type = models.IntegerField(choices=FAV_TYPE, default=1, verbose_name="收藏类型", help_text="收藏类型")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程", help_text="收藏的课程")

    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text="添加时间")

    class Meta:
        verbose_name = "用户收藏课程"
        verbose_name_plural = verbose_name
        unique_together = ("user", "course")

    def __str__(self):
        return self.user.username


class UserFavoriteOrg(models.Model):
    """ 用户收藏机构 """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户", help_text="用户")
    org = models.ForeignKey(CourseOrg, on_delete=models.CASCADE, verbose_name="机构", help_text="收藏的机构")

    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text="添加时间")

    class Meta:
        verbose_name = "用户收藏机构"
        verbose_name_plural = verbose_name
        unique_together = ("user", "org")

    def __str__(self):
        return self.user.username


class UserFavoriteSketch(models.Model):
    """ 用户收藏作品 """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户", help_text="用户")
    sketch = models.ForeignKey(Sketch, on_delete=models.CASCADE, verbose_name="作品", help_text="收藏的作品")

    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text="添加时间")

    class Meta:
        verbose_name = "用户收藏作品"
        verbose_name_plural = verbose_name
        unique_together = ("user", "sketch")

    def __str__(self):
        return self.user.username


class UserMessage(models.Model):
    """ 用户消息 """
    # default=0,发送给全员的消息，否则是用户的ID
    user = models.IntegerField(default=0, verbose_name="接受用户", help_text="接受用户")
    message = models.CharField(max_length=500, verbose_name="消息内容", help_text="消息内容")
    has_read = models.BooleanField(default=False, verbose_name="是否已读", help_text="是否已读")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text="添加时间")

    class Meta:
        verbose_name = "用户消息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.message


class UserDeadline(models.Model):
    """ 用户使用产品期限"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户", help_text="用户")
    expired_time = models.DateTimeField(default=datetime.strftime(datetime.now() + timedelta(days=7), "%Y-%m-%d"),
                                        verbose_name="使用过期时间", help_text="使用过期时间")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text="添加时间")

    class Meta:
        verbose_name = "用户使用期限"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username


class UserCourse(models.Model):
    """ 用户的学习课程 """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户", help_text="用户")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程", help_text="课程")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text="添加时间")
    deadline = models.ForeignKey(UserDeadline, on_delete=models.CASCADE, null=True, blank=True, verbose_name="过期时间", help_text="过期时间")

    class Meta:
        verbose_name = "用户课程"
        verbose_name_plural = verbose_name
        unique_together = ("user", "course")

    def __str__(self):
        return self.course.name