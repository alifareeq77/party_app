from rest_framework.viewsets import ModelViewSet

from video_app.models import Video
from video_app.serializers import VideoSerializer


class VideoModelView(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = []
    http_method_names = ['get', 'post', 'option']
