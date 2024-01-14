from rest_framework.response import Response
from video_app.models import Video
from .custom_permissions import IsOwnerOrReadOnly
from .models import Party
from .serializers import ReadVideo, PartySerializer, ReadPartySerializer, UpdatePartySerializer
from rest_framework import generics, status, viewsets
from rest_framework.permissions import IsAuthenticated


class PartyRoomView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Party.objects.all()
    http_method_names = ['get', 'put', 'delete']
    serializer_class = ReadPartySerializer
    lookup_field = 'slug'

    # def get_queryset(self):
    #     return Party.objects.filter(creator=self.request.user)
    def get_serializer_class(self):
        if self.request.method == "GET":
            return ReadPartySerializer
        elif self.request.method == "PUT":
            return UpdatePartySerializer

    def perform_update(self, serializer):
        serializer.save(partial=True)


class PartyViewSet(viewsets.ModelViewSet):
    model = Party
    http_method_names = ['post']
    serializer_class = PartySerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = PartySerializer(context={"request": request}, data=data)
        if serializer.is_valid():
            print(serializer.validated_data)
            new_party = Party.objects.create(**serializer.validated_data)
            print(new_party)
            new_party.save()
            return Response(ReadPartySerializer(instance=new_party).data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
