# Generated by Django 5.0.1 on 2024-01-12 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='video_slug',
            field=models.SlugField(default=12, max_length=500, unique=True),
            preserve_default=False,
        ),
    ]