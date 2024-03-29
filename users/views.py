import django.contrib.auth as django_auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from quizzes.models import Quiz

from .models import Profile
from .utils import get_current_user, validate_new_user


def login(request):
    return render(request, 'users/login.html', {
        'current_user': get_current_user(request)
    })

def logging_in(request):
    username = request.POST['username_input']
    password = request.POST['password_input']
    user = django_auth.authenticate(request, username=username, password=password)
    if user is not None:
        django_auth.login(request, user)
        return HttpResponseRedirect(reverse('users:profile', args=(username,)))
    else:
        return render(request, 'users/login.html', {
            'current_user': get_current_user(request),
            'error_messages': ['User not found.']
        })

@login_required
def logout(request):
    django_auth.logout(request)
    return HttpResponseRedirect('')

def register(request):
    return render(request, 'users/register.html', {
        'current_user': get_current_user(request)
    })

def registering(request):
    new_username = request.POST['username_input']
    new_password = request.POST['password_input']
    confirm_password = request.POST['password_confirm']

    error_messages = validate_new_user(new_username, new_password, confirm_password)
    if error_messages != []:
        return render(request, 'users/register.html', {
            'current_user': get_current_user(request),
            'error_messages': error_messages
        })

    new_user = User(username=new_username, first_name='NONE', last_name='NONE', email='DONOTSEND@gmail.com')
    new_user.set_password(new_password)
    new_user.save()

    django_auth.login(request, new_user)

    return HttpResponseRedirect(reverse('users:profile', args=(new_username,)))

def profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'users/profile.html', {
        'current_user': get_current_user(request),
        'user': user
    })

def ajax_profile_update(request):
    new_description = request.POST['description']
    current_user = get_current_user(request)
    current_user.profile.description = new_description
    current_user.save()
    return HttpResponse()

def own_quizzes(request, username):
    user = get_object_or_404(User, username=username)
    quizzes = user.authored_set.all()[::-1]
    return render(request, 'users/quizzes.html', {
        'current_user': get_current_user(request),
        'user': user,
        'quizzes': quizzes
    })

def taken_quizzes(request, username):
    user = get_object_or_404(User, username=username)
    quizzes = user.taken_set.all()[::-1]
    return render(request, 'users/quizzes.html', {
        'current_user': get_current_user(request),
        'user': user,
        'quizzes': quizzes
    })
