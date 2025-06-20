from django.contrib import admin

from .models import Menu, Booking

# Register your models here.
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    search_fields = ['name']
    ordering = ['name']

@admin.register(Booking)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'guest_number', 'comment']
    search_fields = ['first_name', 'last_name']
    ordering = ['first_name']

