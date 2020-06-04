from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [
    path('register', register, name='register'),
    path('referrer/<str:username>', register_referred, name='register_referred'),
    path('login', login, name='login'),
]
