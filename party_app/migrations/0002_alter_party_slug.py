# Generated by Django 5.0.1 on 2024-01-13 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('party_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
    ]
