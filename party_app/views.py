from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from video_app.models import Video
from video_app.serializers import VideoSerializer
from .models import Party
from .serializers import PartySerializer, ReadVideo
from rest_framework import generics, viewsets, status
from rest_framework.permissions import IsAuthenticated


class PartyRoomView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ReadVideo
    queryset = Video.objects.all()
    http_method_names = ['get']

    def get_queryset(self):
        video_id = Party.objects.filter(slug=self.kwargs.get('slug'))[0].video.id
        return get_object_or_404(Video, id=video_id)


class SlugView(ModelViewSet):
    model = Party


class SlugViewData(APIView):
    def get(self, request, id, *args, **kwargs):
        # Perform any logic to retrieve your object based on the ID
        # For example, you might fetch data from a database or another source
        your_object_data = {
            'id': id,

        }
        serializer = ReadVideo(data=your_object_data)
        if serializer.is_valid():
            video = Video.objects.get(id=your_object_data['id'])
            print(video)
            p = Party.objects.create(video=video,creator=request.user)
            p.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
