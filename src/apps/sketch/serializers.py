from rest_framework import serializers

from .models import Sketch
from users.serializers import UserDetailSerializer


class SketchDetailSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer(many=False)

    class Meta:
        model = Sketch
        fields = "__all__"


class SketchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sketch
        fields = "__all__"
