from django.shortcuts import render
import sys
sys.path.append("..")
import book
from book.models import Book

# Create your views here.
def summary(request, locator):
    summary_book = Book.objects.filter(locator=locator)
    return render(request, "summary/summary.html",  {'summary_book':summary_book})