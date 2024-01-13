from django.db import models
from video_app.models import Video
from django.utils.text import slugify
from django.conf import settings
from django.utils.crypto import get_random_string


def unique_slugify(instance, string_to_slugify, restricted_slugs=[]):
    # Slug encryption making
    slug_value = slugify(string_to_slugify)
    model = instance.__class__
    hardcoded_restricted_slugs = ['add', 'exec', 'all']
    restricted_slugs = restricted_slugs + hardcoded_restricted_slugs
    if slug_value in restricted_slugs:
        slug_value = slug_value + get_random_string(length=4)
    if model.objects.filter(slug=slug_value).exists():
        slug_value = unique_slugify(instance, slug_value + get_random_string(length=4))
    return slug_value


class Party(models.Model):
    # Party Room Model
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    create_datetime = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    state = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Party Room Slug Generator Function
        slug = get_random_string(length=10)
        self.slug = unique_slugify(self, slug)
        super().save(*args, **kwargs)
