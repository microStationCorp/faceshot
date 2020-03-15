from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import uploadPhotoForm
from django.contrib import messages
from .models import Seasons

# Create your views here.


@login_required(login_url='../login')
def addphoto(response):
    if response.method == 'POST':
        form = uploadPhotoForm(response.POST, response.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            image = response.FILES['image']
            upload.image = image
            upload.uploader = response.user
            upload.season = Seasons.objects.all().last()
            upload.save()
            messages.info(response, 'Succesfully Uploaded')
            return redirect('../profile')
        else:
            messages.warning(response, 'Invalid upload')
            return redirect('../addphoto')
    else:
        form = uploadPhotoForm()
    return render(response, 'addphoto/addphoto.html', {'form': form})
