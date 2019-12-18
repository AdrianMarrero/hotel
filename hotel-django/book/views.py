from django.shortcuts import render, redirect
from rooms import views as room_views
from .forms import BookForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils import timezone
import random, string
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        prev_form = request.POST
        save_form =  prev_form['save']
        days = prev_form['days']
       
        if save_form == 'False':
            number_room = prev_form['number_room']
            data_room = room_views.Room.objects.get(number_room=number_room)
            request.POST._mutable = True
            request.POST['date_start'] = prev_form['start']
            request.POST['date_end'] = prev_form['end']
            request.POST['n_persons'] = prev_form['persons']
            request.POST['total_price'] = int(data_room.price_room) * int(days)
            request.POST._mutable = False
            return render(request, "book/book.html", {'days':days, 'data_room':data_room, 'form':form})
        elif save_form == 'True':
            number_room = prev_form['number_book_conf']
            data_room = room_views.Room.objects.get(number_room=number_room)
            print(request.POST)
            if form.is_valid():              
                record_book = form.save(commit=False)
                record_book.number_book = number_room
                locator_id = random_id()
                record_book.locator = locator_id
                record_book.user_email = request.user.email
                record_book.save()
                form.save_m2m()
                return redirect('summary', locator=locator_id)
            else:
                print(form.errors)
                return render(request, "book/book.html", {'days':days, 'data_room':data_room, 'form':form})    
        else:
            print('por el final')
            form = BookForm()
            return render(request, "book/book.html",{'form':form})

def random_id(lenght=20):
    return ''.join(random.choice(string.ascii_letters + string.digits) for x in range(lenght))