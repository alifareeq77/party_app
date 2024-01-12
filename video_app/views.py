from django.shortcuts import get_object_or_404, render, redirect
from .models import Video
from .forms import VideoForm  # Create a form for handling video uploads
from .serializers import VideoSerializer
from rest_framework import generics



class VideoUploadView(generics.CreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.creator_id = 1
            form.creator_id=1
            form.save()
            return redirect('video_list')  # Redirect to a video list view after successful upload
    else:
        form = VideoForm()

    return render(request, 'upload_video.html', {'form': form})

def view_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    return render(request, 'view_video.html', {'video': video})
