from django.template.defaulttags import url
from django.urls import include, path
from rest_framework import routers

from .views import PartyRoomView, SlugView, SlugViewData

router = routers.SimpleRouter()

router.register('slug', SlugView, basename='slug')
urlpatterns = [
    path('room/<slug:slug>', PartyRoomView.as_view()),
    path('slug/<int:id>/', SlugViewData.as_view(), name='slug'),
] + router.urls
