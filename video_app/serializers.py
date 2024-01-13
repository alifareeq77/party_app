from rest_framework import serializers

from .models import Video


class VideoSerializer(serializers.ModelSerializer):
    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Video
        fields = ("creator", "video_file", "title", "description", "create_datetime")


class ReadVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id',)
