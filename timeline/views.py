from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from registerpage.models import extraUserData
from django.contrib.auth.models import User
from addphoto.models import UploadedPhoto
from django.http import HttpResponse, JsonResponse
# Create your views here.


def get_image(User_id, user_last_voted_pic_id):
    empty_flag = True
    user_last_voted_pic_id += 1
    while user_last_voted_pic_id <= UploadedPhoto.objects.all().last().id:
        if UploadedPhoto.objects.filter(id=user_last_voted_pic_id).count() != 0 and UploadedPhoto.objects.get(id=user_last_voted_pic_id).uploader_id != User_id:
            empty_flag = False
            break
        user_last_voted_pic_id += 1
    if empty_flag == False:
        img = UploadedPhoto.objects.get(id=user_last_voted_pic_id)
        return img
    else:
        return None


@login_required(login_url='../login')
def timelinepage(response):
    user = User.objects.get(id=response.user.id)
    user_data = extraUserData.objects.get(user=user)
    img = get_image(response.user.id, user_data.last_voted_pic_id)
    if img != None:
        context = {
            'img': img
        }
        return render(response, 'timeline/timeline.html', context)
    else:
        return render(response, 'timeline/timeline.html', {'empty': True})


@login_required(login_url='../login')
def voted(response):
    if response.method == "POST" and response.is_ajax():
        user = User.objects.get(id=response.user.id)
        user_data = extraUserData.objects.get(user=user)
        user_data.last_voted_pic_id = int(response.POST['image_id'])
        user_data.save()

        img_id = int(response.POST['image_id'])
        reacted_img = UploadedPhoto.objects.get(id=img_id)
        if response.POST['reaction'] == 'haha':
            reacted_img.haha_count += 1
        elif response.POST['reaction'] == 'fire':
            reacted_img.fire_count += 1
        elif response.POST['reaction'] == 'poop':
            reacted_img.poop_count += 1
        reacted_img.save()

        img = get_image(response.user.id, user_data.last_voted_pic_id)

        if img != None:
            context = {
                'url': img.image.url,
                'image_id': img.id
            }
            return JsonResponse(context)
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
