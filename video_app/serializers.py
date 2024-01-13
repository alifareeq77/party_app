from rest_framework import serializers
from .models import Video

class VideoSerializer(serializers.ModelSerializer):
    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Video
        fields = ("video_file","title","description","creator","create_datetime")