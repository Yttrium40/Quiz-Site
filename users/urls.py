from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logging_in/', views.logging_in, name='logging_in'),
    path('logout', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('registering/', views.registering, name='registering'),
    path('profile/<username>/', views.profile, name='profile'),
    path('ajax/profile_update/', views.ajax_profile_update, name='ajax_profile_update'),
]
