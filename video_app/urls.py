from django.urls import include, path
from rest_framework import routers

from video_app.views import VideoModelView
router = routers.SimpleRouter()
router.register(r'video', VideoModelView)
urlpatterns = []+router.urls
