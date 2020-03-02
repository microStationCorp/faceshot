from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from addphoto.models import UploadedPhoto

# Create your views here.


@login_required(login_url='../login')
def poll(response):
    return render(response, 'poll/poll.html')


@login_required(login_url='../login')
def pollAjax(response):
    if response.method == "GET" and response.is_ajax():
        order_category = response.GET['rank_order_name']
        context = []
        if order_category == 'RF':
            for f in UploadedPhoto.objects.all().order_by('-fire_count')[:5]:
                context.append({
                    'url': f.image.url,
                    'count': f.fire_count,
                    'caption': f.caption,
                    'uploader': f.uploader.username
                })
        elif order_category == 'RH':
            for f in UploadedPhoto.objects.all().order_by('-haha_count')[:5]:
                context.append({
                    'url': f.image.url,
                    'count': f.haha_count,
                    'caption': f.caption,
                    'uploader': f.uploader.username
                })
        elif order_category == 'RP':
            for f in UploadedPhoto.objects.all().order_by('-poop_count')[:5]:
                context.append({
                    'url': f.image.url,
                    'count': f.poop_count,
                    'caption': f.caption,
                    'uploader': f.uploader.username
                })
        return JsonResponse(context, safe=False)
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
