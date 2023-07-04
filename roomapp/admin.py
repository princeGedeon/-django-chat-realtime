from django.contrib import admin

# Register your models here.
from roomapp.models import Room


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['name','pk']