from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from video_app.models import Video
from video_app.serializers import VideoSerializer, ShowVideoSerializer


class VideoModelView(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'option']

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ShowVideoSerializer
        else:
            return VideoSerializer

    def get_queryset(self):
        queryset = Video.objects.filter(creator=self.request.user)


def index_view(request):
    return render(request, 'video_app/index.html')
