from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.validators import FileExtensionValidator



#function for naming videofiles according to it upload datetime stamp
def upload_to(instance, filename):
    timestamp = timezone.now().strftime('%Y%m%d%H%M%S')
    return f'uploads/{timestamp}_{filename}'


#main video model
class Video(models.Model):
    video_file = models.FileField(
        upload_to=upload_to,
        null=False,
        blank=False,
        validators=[
            FileExtensionValidator(allowed_extensions=['mp4', 'mpg', 'mpeg'])
        ],
        help_text='Upload only MP4, MPG, or MPEG files'
    )
    title = models.CharField(max_length=150, null=False, blank=False)
    description = models.CharField(max_length=255) 
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    create_datetime = models.DateTimeField(auto_now_add=True)
