from django.shortcuts import get_object_or_404, render

from .models import Party
from .serializers import PartySerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class PartyRoomView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PartySerializer
    queryset = Party.objects.all()
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Party, slug=slug)