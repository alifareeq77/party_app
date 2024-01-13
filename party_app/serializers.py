from rest_framework import serializers
from .models import Party
from video_app.serializers import ReadVideoSerializer, VideoSerializer


class PartySerializer(serializers.ModelSerializer):
    # Serializer for the Party model.
    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())
    video = ReadVideoSerializer()

    class Meta:
        model = Party
        fields = ("video", "creator")


class ReadVideo(serializers.Serializer):
    # Serializer for reading video details.
    id = serializers.IntegerField()
