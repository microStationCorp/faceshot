from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from addphoto.models import UploadedPhoto

# Create your views here.


@login_required(login_url='../login')
def userprofile(response):
    imgs = UploadedPhoto.objects.filter(uploader_id=response.user.id).order_by('-dateOfPost')
    context = {
        'imgs': imgs
    }
    return render(response, 'userprofile/profile.html', context)
