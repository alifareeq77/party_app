from rest_framework import serializers
from .models import Video

class VideoSerializer(serializers.ModelSerializer):
    # Serializer for the Video model
    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Video
        fields = ("creator", "video_file", "title", "description", "create_datetime")

class ReadVideoSerializer(serializers.ModelSerializer):
    # Serializer for reading video details
    class Meta:
        model = Video
        fields = ('id',)
