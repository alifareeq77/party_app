from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from party_app.models import Party
from video_app.models import Video
from video_app.serializers import VideoSerializer


class VideoModelView(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'option']


def index_view(request):
    return render(request, 'video_app/index.html')
