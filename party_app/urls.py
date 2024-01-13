from django.template.defaulttags import url
from django.urls import include, path
from .views import PartyRoomView
urlpatterns = [
    path('room/<slug:slug>', PartyRoomView.as_view(), ),
]

