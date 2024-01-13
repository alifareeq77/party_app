from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics, viewsets, status
from rest_framework.permissions import IsAuthenticated
from video_app.models import Video
from video_app.serializers import VideoSerializer
from .models import Party
from .serializers import PartySerializer, ReadVideo


class PartyRoomView(generics.RetrieveAPIView):
    # API view for retrieving a party room with video details.
    permission_classes = (IsAuthenticated,)
    serializer_class = ReadVideo
    queryset = Video.objects.all()
    http_method_names = ['get']

    def get_queryset(self):
        # Retrieve the queryset for the party room.
        video_id = Party.objects.filter(slug=self.kwargs.get('slug'))[0].video.id
        return get_object_or_404(Video, id=video_id)


class SlugView(ModelViewSet):
    # Viewset for handling CRUD operations on Party model.
    model = Party


class SlugViewData(APIView):
    # API view for handling data related to party slugs.
    def get(self, request, id, *args, **kwargs):
        # Handle GET request to create a new party with associated video.
        video_data = {'id': id}
        serializer = ReadVideo(data=video_data)

        if serializer.is_valid():
            video = Video.objects.get(id=video_data['id'])
            print(video)
            p = Party.objects.create(video=video, creator=request.user)
            p.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
