from django.shortcuts import render
import sys
sys.path.append("..")
import book
from book.models import Book

# Create your views here.
def management(request):
    all_books = Book.objects.all()
    return render(request, "management/management.html", {'all_books':all_books})
