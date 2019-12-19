from django.shortcuts import render
import sys
sys.path.append("..")
import book
from book.models import Book

# Create your views here.
def mybooks(request):
    if request.method == 'POST':
        prev_form = request.POST
        user_email_form = prev_form['email']
        my_books = Book.objects.filter(user_email=user_email_form)
    return render(request, "mybooks/mybooks.html", {'my_books':my_books})