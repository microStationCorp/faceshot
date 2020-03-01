# from django.contrib.auth.forms import forms
from django.forms import ModelForm
from .models import UploadedPhoto


class uploadPhotoForm(ModelForm):
    class Meta:
        model = UploadedPhoto
        fields = [
            "caption",
            "image"
        ]
