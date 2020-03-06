from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from addphoto.models import UploadedPhoto as up
from django.http import HttpResponse, JsonResponse


# Create your views here.


@login_required(login_url='../login')
def timelinepage(response):
    other_user_img = up.objects.exclude(
        Q(uploader__id=response.user.id) | Q(haha_count__id=response.user.id) | Q(fire_count__id=response.user.id) | Q(
            poop_count__id=response.user.id)).order_by('dateOfPost')
    if other_user_img.count() == 0:
        context = {
            'empty': True
        }
    else:
        context = {
            'img':other_user_img[0]
        }
    return render(response, 'timeline/timeline.html', context)
