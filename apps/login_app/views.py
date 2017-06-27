from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    print 'index works'
    if 'user_id' in request.session:
        return redirect(reverse('travel:index'))
    else:
        return render(request, 'login_app/index.html')

def register(request):
    print 'register works'
    result = User.objects.register(request.POST)
    if result[0] == True:
        request.session['user_id'] = result[1].id
        messages.success(request, "Sucessfully Registered")
        return redirect(reverse('login:index'))
    else:
        for error in result[1]:
            messages.error(request, error)
        return redirect(reverse('login:index'))

def login(request):
    print 'login works'
    result = User.objects.login(request.POST)
    if result[0] == True:
        request.session['user_id'] = result[1].id
        return redirect(reverse('travel:index'))
    else:
        for error in result[1]:
            messages.error(request, error)
        return redirect(reverse('login:index'))

def logout(request):
    print 'logout works'
    if 'user_id' in request.session:
        del request.session['user_id']
        messages.success(request, "Sucessfully Logged Out")
        return redirect(reverse('login:index'))
