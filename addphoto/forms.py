# from django.contrib.auth.forms import forms
from django.forms import ModelForm
from .models import UploadedPhoto
from django import forms


class uploadPhotoForm(ModelForm):
    class Meta:
        model = UploadedPhoto
        widgets = {
            'caption': forms.Textarea(attrs={'rows': 3, 'cols': 15})
        }

        fields = [
            "image",
            "caption",
        ]
