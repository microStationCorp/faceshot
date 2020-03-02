from django.contrib import admin
from .models import UploadedPhoto
from django.contrib.admin.options import ModelAdmin
# Register your models here.


class UploadAdmin(ModelAdmin):
    list_display = [
        "caption",
        "dateOfPost",
        "fire_count",
        "poop_count",
        "haha_count"]


admin.site.register(UploadedPhoto, UploadAdmin)
