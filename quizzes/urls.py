from django.urls import path

from . import views

app_name = 'quizzes'
urlpatterns = [
    path('create/', views.create, name='create'),
    path('creating/', views.creating, name='creating'),
    path('<int:pk>/details/', views.details, name='details'),
]
