from django.shortcuts import render

# Create your views here.


def timelinepage(response):
    return render(response, 'timeline/timeline.html')
