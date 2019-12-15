from django.shortcuts import render
from .models import Room

# Create your views here.
def rooms(request):
    return render(request,"rooms/rooms.html")