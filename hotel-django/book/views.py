from django.shortcuts import render, redirect
from rooms import views as room_views
from .forms import BookForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils import timezone
# Create your views here.

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
                record_book.save()
                form.save_m2m()
                return redirect('home')
            else:
                print(form.errors)
                return render(request, "book/book.html", {'days':days, 'data_room':data_room, 'form':form})    
        else:
            print('por el final')
            form = BookForm()
            return render(request, "book/book.html",{'form':form})

