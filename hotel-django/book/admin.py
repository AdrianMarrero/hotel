from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'number_book', 'date_start', 'date_end','days','n_persons','total_price', 'locator')


# Register your models here.
admin.site.register(Book, BookAdmin)