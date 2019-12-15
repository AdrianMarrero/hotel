from django.shortcuts import render
from django.contrib.auth.models import User
from rooms import views as room_views

# Create your views here.
def home(request):
    rooms = room_views.Room.objects.all()
    singles_room = rooms.filter(room_type='1').count()
    double_room = rooms.filter(room_type='2').count()
    triple_room = rooms.filter(room_type='3').count()
    quadruple = rooms.filter(room_type='4').count()
    return render(request, "core/index.html", {'rooms':rooms, 'singles_room':singles_room,
    'double_room':double_room, 'triple_room':triple_room, 'quadruple':quadruple })