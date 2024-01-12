from django.template.defaulttags import url
from django.urls import include, path
from video_app.views import VideoUploadView, upload_video, view_video
urlpatterns = [
    path('upload/', upload_video, name='upload_video'),
    path('video/<int:video_id>/', view_video, name='view_video'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('api/upload/', VideoUploadView.as_view(), name='video_upload_api'),
    
]

