from rest_framework import serializers
from .models import Party
from video_app.serializers import VideoSerializer

class PartySerializer(serializers.ModelSerializer):
    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())
    video_url = VideoSerializer(read_only=True)
    class Meta:
        model = Party
        fields = ("video_url","creator")