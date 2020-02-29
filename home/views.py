from django.shortcuts import render, redirect

# Create your views here.


def homepage(response):
    if response.user.is_authenticated:
        return redirect('../timeline')
    return render(response, 'home/home.html')
