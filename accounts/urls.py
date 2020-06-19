from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [
    path('register', register, name='register'),
    path('referrer/<str:username>', register_referred, name='register_referred'),
    path('login', login_page, name='login'),
    path('logout', logout_user, name='logout'),
    path('home', home_page, name='home'),
]
