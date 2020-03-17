from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
import os
from django.utils import timezone


# Create your models here.

class Seasons(models.Model):
    season_number = models.IntegerField(default=0)


def get_image_path(instance, filename):
    return os.path.join(f'{Seasons.objects.all().last().season_number}', str(instance.uploader.id), filename)


class UploadedPhoto(models.Model):
    dateOfPost = models.DateTimeField(default=timezone.now)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    season = models.ForeignKey(Seasons, on_delete=models.CASCADE)
    caption = models.TextField(blank=True, null=True)
    image = ResizedImageField(size=[500, 500], upload_to=get_image_path)
    haha_count = models.ManyToManyField(
        User, related_name="haha_count", blank=True)
    fire_count = models.ManyToManyField(
        User, related_name="fire_count", blank=True)
    poop_count = models.ManyToManyField(
        User, related_name="poop_count", blank=True)
    noex_count = models.ManyToManyField(
        User, related_name="noex_count", blank=True)
    hahaStat = models.BigIntegerField(default=0)
    fireStat = models.BigIntegerField(default=0)
    poopStat = models.BigIntegerField(default=0)
    noexStat = models.BigIntegerField(default=0)
