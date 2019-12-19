from django.shortcuts import render
from django.contrib.auth.models import User
from rooms import views as room_views
import sys
sys.path.append("..")
import book
from book.models import Book
from datetime import datetime, timedelta
from django.db import connection
from django.utils.dateparse import parse_date
import datetime as dt

# Create your views here.
def home(request):
    search_form = request.GET
    days = 0
    user_recepcionista = 'Recepcionista'
    rooms = {}
    if request.method == 'GET' and search_form:
        n_persons = search_form['n_persons']
        days = get_days(search_form)
        fecha_start = datetime.strptime(search_form['date_start'], "%d/%m/%Y").date()
        fecha_end = datetime.strptime(search_form['date_end'], "%d/%m/%Y").date()
        rooms = query_rooms(n_persons, fecha_start, fecha_end)

    return render(request, "core/index.html", {'rooms':rooms, 'search_form':search_form, 'days':days, 'user_recepcionista':user_recepcionista })


def get_days(search_form):
    fecha_cad1 = search_form['date_start']
    fecha_cad2 = search_form['date_end']
    fecha1 = datetime.strptime(fecha_cad1, '%d/%m/%Y')
    fecha2 = datetime.strptime(fecha_cad2, '%d/%m/%Y')
    return (fecha2 - fecha1).days



def query_rooms(n_persons, fecha_start, fecha_end):
    rooms = {}
    
    query_base_str = """SELECT rooms_room.room_type, rooms_room.price_room,
                                    rooms_room.image, rooms_room.name_room, rooms_room.number_room
                                    FROM rooms_room LEFT JOIN book_book ON rooms_room.number_room = book_book.number_book 
                                    AND book_book.date_start >=%s  and date_end <=%s 
                                    WHERE book_book.number_book is null"""

    if n_persons == '1':
        rooms = room_views.Room.objects.raw(query_base_str, [fecha_start, fecha_end])
    elif n_persons == '2':
        query_extra  = """ AND (rooms_room.room_type= %sOR rooms_room.room_type= %s OR rooms_room.room_type= %s)"""
        print(query_base_str + query_extra)
        rooms = room_views.Room.objects.raw(query_base_str + query_extra, [fecha_start, fecha_end, 3,4,2]) 
    elif n_persons == '3':
        query_extra = """ AND (rooms_room.room_type= %s OR rooms_room.room_type= %s)"""
        rooms = room_views.Room.objects.raw(query_base_str + query_extra, [fecha_start, fecha_end, 3, 4]) 
    elif  n_persons == '4':
        query_extra = """  AND rooms_room.room_type= %s"""
        rooms = room_views.Room.objects.raw(query_base_str + query_extra, [fecha_start, fecha_end, n_persons])
    return rooms