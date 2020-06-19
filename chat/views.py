from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    return render(request, 'chat/index.html', {})


def room(request, room_name):
    room = Room.objects.get(room_name=room_name).room_name

    return render(request, 'chat/room.html', {'room_name': room})
