from django.shortcuts import render

# Create your views here.
def registerpage(response):
    return render(response, 'registerpage/register.html')