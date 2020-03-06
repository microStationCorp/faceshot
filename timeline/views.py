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
            'img': other_user_img[0]
        }
    return render(response, 'timeline/timeline.html', context)


@login_required(login_url='../login')
def voted(response):
    if response.method == "POST" and response.is_ajax():
        user = User.objects.get(id=response.user.id)

        img_id = int(response.POST['image_id'])
        reacted_img = up.objects.get(id=img_id)
        if response.POST['reaction'] == 'haha':
            reacted_img.haha_count.add(user)
            reacted_img.hahaStat = reacted_img.haha_count.all().count()
            reacted_img.save()
        elif response.POST['reaction'] == 'fire':
            reacted_img.fire_count.add(user)
            reacted_img.fireStat = reacted_img.fire_count.all().count()
            reacted_img.save()
        elif response.POST['reaction'] == 'poop':
            reacted_img.poop_count.add(user)
            reacted_img.poopStat = reacted_img.poop_count.all().count()
            reacted_img.save()

        other_user_img = up.objects.exclude(Q(uploader__id=response.user.id) | Q(haha_count__id=response.user.id) | Q(
            fire_count__id=response.user.id) | Q(poop_count__id=response.user.id)).order_by('dateOfPost')

        if other_user_img.count() != 0:
            context = {
                'url': other_user_img[0].image.url,
                'image_id': other_user_img[0].id
            }
        else:
            context = {
                'url': 'None'
            }
        return JsonResponse(context)
    else:
        return HttpResponse('''<h1 style="border-bottom: 1px solid #aaa; padding: 10px" > Not Found(  # 404)</h1>
        <div class="alert alert-danger" >
            Page not found. </div >
        <p>
            The above error occurred while the Web server was processing your request.
        </p>
        <p>
            Please contact us if you think this is a server error. Thank you.
        </p>''')
