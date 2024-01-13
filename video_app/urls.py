from django.template.defaulttags import url
from django.urls import include, path
from rest_framework import routers

from video_app.views import VideoModelView, index_view

router = routers.SimpleRouter()
router.register(r'video', VideoModelView)
urlpatterns = [
    path('test/', index_view, name='index')
              ]+router.urls
