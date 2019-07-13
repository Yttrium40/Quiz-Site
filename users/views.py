from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
import django.contrib.auth as django_auth
from django.contrib.auth.models import User

from .models import Profile
from .utils import validate_new_user

def login(request):
    return render(request, 'users/login.html', {})

def logging_in(request):
    username = request.POST['username_input']
    password = request.POST['password_input']
    user = django_auth.authenticate(request, username=username, password=password)
    if user is not None:
        django_auth.login(request, user)
        return HttpResponseRedirect(reverse('users:profile', args=(username,)))
    else:
        return render(request, 'users/login.html', {'error_messages': ['User not found.']})

def register(request):
    return render(request, 'users/register.html', {})

def registering(request):
    new_username = request.POST['username_input']
    new_password = request.POST['password_input']
    confirm_password = request.POST['password_confirm']

    error_messages = validate_new_user(new_username, new_password, confirm_password)
    if error_messages != []:
        return render(request, 'users/register.html', {'error_messages': error_messages})

    new_user = User(username=new_username, first_name='NONE', last_name='NONE', email='DONOTSEND@gmail.com')
    new_user.set_password(new_password)
    new_user.save()

    django_auth.login(request, new_user)

    return HttpResponseRedirect(reverse('users:profile', args=(new_username,)))

def profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'users/profile.html', {'user': user})
