from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from addphoto.models import UploadedPhoto


# Create your views here.


@login_required(login_url='../login')
def poll(response):
    hahaList = []
    poopList = []
    fireList = []

    for f in UploadedPhoto.objects.all().order_by('-hahaStat')[:10]:
        hahaList.append({
            'url': f.image.url,
            'count': f.haha_count.all().count(),
            'caption': f.caption,
            'uploader': f.uploader.username
        })
    for f in UploadedPhoto.objects.all().order_by('-fireStat')[:10]:
        fireList.append({
            'url': f.image.url,
            'count': f.fire_count.all().count(),
            'caption': f.caption,
            'uploader': f.uploader.username
        })
    for f in UploadedPhoto.objects.all().order_by('-poopStat')[:10]:
        poopList.append({
            'url': f.image.url,
            'count': f.poop_count.all().count(),
            'caption': f.caption,
            'uploader': f.uploader.username
        })

    context = {
        'haha': hahaList,
        'poop': poopList,
        'fire': fireList
    }
    return render(response, 'poll/poll.html', context)

