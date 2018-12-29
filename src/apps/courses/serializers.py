from rest_framework import serializers

from .models import Course, LessonContent, Lesson, Video, CourseResource


class CourseSerializer(serializers.ModelSerializer):
    """ 课程序列化 """
    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(serializers.ModelSerializer):
    """ 章节序列化 """
    course = CourseSerializer()

    class Meta:
        model = Lesson
        fields = "__all__"


class LessonContentSerializer(serializers.ModelSerializer):
    """ 章节内容序列化 """
    lesson = LessonSerializer()

    class Meta:
        model = LessonContent
        fields = "__all__"


class VideoSerializer(serializers.ModelSerializer):
    """ 章节视频序列化 """
    lesson = LessonSerializer()

    class Meta:
        model = Video
        fields = "__all__"


class CourseResourceSerializer(serializers.ModelSerializer):
    """ 课程资源序列化 """
    course = CourseSerializer()

    class Meta:
        model = CourseResource
        fields = "__all__"
