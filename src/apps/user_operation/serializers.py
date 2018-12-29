from datetime import datetime, timedelta

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import UserEnroll, SalesInfo, UserFavoriteCourse, UserCourse
from .models import UserDeadline, UserFavoriteOrg, UserFavoriteSketch
from courses.serializers import CourseSerializer
from sketch.models import Sketch


class UserEnrollDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEnroll
        fields = "__all__"


class UserEnrollSerializer(serializers.ModelSerializer):
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = UserEnroll
        fields = ("id", "name", "birthday", "gender", "mobile", "address", "school", "enroll", "msg_ad", "remark", "add_time")


class SalesInfoDetailSerializer(serializers.ModelSerializer):
    course = CourseSerializer(many=False)
    student = UserEnrollSerializer(many=False)

    class Meta:
        model = SalesInfo
        fields = "__all__"


class SalesInfoSerializer(serializers.ModelSerializer):
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = SalesInfo
        fields = "__all__"


class UserFavCourseDetailSerializer(serializers.ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = UserFavoriteCourse
        fields = ("course", "id")


class UserFavCourseSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = UserFavoriteCourse
        validators = [
            UniqueTogetherValidator(
                queryset=UserFavoriteCourse.objects.all(),
                fields=('user', 'course'),
                message="已经收藏"
            )
        ]
        fields = ("user", "course", "id")


class UserSketchSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Sketch
        fields = "__all__"


class UserCourseDetailSerializer(serializers.ModelSerializer):
    course = CourseSerializer(many=False)

    class Meta:
        model = UserCourse
        fields = "__all__"


class UserCourseSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = UserCourse
        validators = [
            UniqueTogetherValidator(
                queryset=UserCourse.objects.all(),
                fields=('user', 'course'),
                message="课程已经购买"
            )
        ]
        fields = "__all__"


class UserDeadlineSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    # expired_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    def create(self, validated_data):
        user = self.context["request"].user
        deadline = validated_data["expired_time"]
        expired_time = datetime.strptime(deadline, "%Y-%m-%d %H:%M")
        existed = UserDeadline.objects.filter(user=user)

        if existed:
            existed = existed[0]
            existed.expired_time = datetime.strftime(expired_time + timedelta(days=30), "%Y-%m-%d")
            existed.save()
        else:
            existed.expired_time = expired_time
            print("**\n**\n** %s **\n***\n") % expired_time
            existed.save()

        return existed

    class Meta:
        model = UserDeadline
        fields = "__all__"
