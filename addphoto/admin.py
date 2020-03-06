from django.contrib import admin
from .models import UploadedPhoto
from django.contrib.admin.options import ModelAdmin
# Register your models here.


class UploadAdmin(ModelAdmin):
    list_display = [
        "caption",
        "dateOfPost",
    ]

admin.site.register(UploadedPhoto, UploadAdmin)
