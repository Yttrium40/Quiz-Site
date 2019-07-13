from django.shortcuts import render
from users.utils import get_current_user

def home(request):
    return render(request, 'QuizSite/home.html', {
        'current_user': get_current_user(request)
    })
