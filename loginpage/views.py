from django.shortcuts import render,redirect
from .forms import loginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def loginpage(response):
    if response.method == 'POST':
        form = loginForm(response.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(response, username=username, password=password)
            if user is not None:
                login(response, user)
                return redirect('../timeline')
            else:
                messages.warning(response, 'invalid Username or Password')
                return redirect('../login')
    else:
        form = loginForm()
    return render(response, 'loginpage/login.html', {'form': form})
