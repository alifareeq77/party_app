from rest_framework import serializers
from video_app.models import Video
from video_app.serializers import ShowVideoSerializer
from .models import Party


class PartySerializer(serializers.ModelSerializer):
    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())
    video = serializers.PrimaryKeyRelatedField(many=False, queryset=Video.objects.all())

    class Meta:
        model = Party
        fields = ("video", "creator")


class UpdatePartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = ('state',)


class ReadPartySerializer(serializers.ModelSerializer):
    video = ShowVideoSerializer(read_only=True, many=False)

    class Meta:
        model = Party
        fields = '__all__'
        exclude = 'creator'


class ReadVideo(serializers.Serializer):
    id = serializers.IntegerField()
