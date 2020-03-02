from django.contrib import admin
from .models import extraUserData
from django.contrib.admin.options import ModelAdmin
# Register your models here.

class ExtraAdmin(ModelAdmin):
    list_display=[
        "user",
        "gender",
        "last_voted_pic_id"
    ]

admin.site.register(extraUserData,ExtraAdmin)
