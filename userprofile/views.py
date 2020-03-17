from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from addphoto.models import UploadedPhoto, Seasons

# Create your views here.


@login_required(login_url='../login')
def userprofile(response):
    imgs = UploadedPhoto.objects.filter(
        uploader_id=response.user.id, season=Seasons.objects.all().last()).order_by('-dateOfPost')

    img_list = []

    for img in imgs:
        img_list.append({
            'caption': img.caption,
            'url': img.image.url,
            'hahaStat': img.hahaStat,
            'fireStat': img.fireStat,
            'poopStat': img.poopStat,
            'noexStat': img.noexStat,
            'hahaRank': list(UploadedPhoto.objects.filter(season=Seasons.objects.all().last()).order_by('-hahaStat').values_list('id', flat=True)).index(img.id)+1,
            'fireRank': list(UploadedPhoto.objects.filter(season=Seasons.objects.all().last()).order_by('-fireStat').values_list('id', flat=True)).index(img.id)+1,
            'poopRank': list(UploadedPhoto.objects.filter(season=Seasons.objects.all().last()).order_by('-poopStat').values_list('id', flat=True)).index(img.id)+1,
            'noexRank': list(UploadedPhoto.objects.filter(season=Seasons.objects.all().last()).order_by('-noexStat').values_list('id', flat=True)).index(img.id)+1,
        })

    return render(response, 'userprofile/profile.html', {'img_list': img_list})
