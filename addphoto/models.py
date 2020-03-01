from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
import os

# Create your models here.


def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.uploader.id), filename)


class UploadedPhoto(models.Model):
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.CharField(max_length=140, blank=True, null=True)
    image = ResizedImageField(size=[500,500],upload_to=get_image_path)
