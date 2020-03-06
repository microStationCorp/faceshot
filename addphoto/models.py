from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
import os
from django.utils import timezone


# Create your models here.


def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.uploader.id), filename)


class UploadedPhoto(models.Model):
    dateOfPost = models.DateTimeField(default=timezone.now)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.CharField(max_length=140, blank=True, null=True)
    image = ResizedImageField(size=[500, 500], upload_to=get_image_path)
    fire_count = models.ManyToManyField(User, related_name="fire_count", blank=True)
    poop_count = models.ManyToManyField(User, related_name="poop_count", blank=True)
    haha_count = models.ManyToManyField(User, related_name="haha_count", blank=True)
