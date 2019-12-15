from django.contrib import admin
from .models import Room

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name_room', 'room_type', 'number_room')

# Register your models here.
admin.site.register(Room, ProjectAdmin)