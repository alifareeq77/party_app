from django.template.defaulttags import url
from django.urls import include, path
from .views import VideoUploadView, upload_video, view_video
urlpatterns = [
    path('up/', upload_video, name='upload_video'),
    path('video/<int:video_id>/', view_video, name='view_video'),
    path('upload/', VideoUploadView.as_view(), name='video_upload_api'),
    
]

