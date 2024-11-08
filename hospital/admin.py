# hospital/admin.py
from django.contrib import admin
from hospital.models import Room, Staff, Equipment, Reservation

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'room_type', 'is_available')
    list_filter = ('room_type', 'is_available')
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    list_filter = ('role',)
    search_fields = ('user__username',)
    ordering = ('user',)

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity')
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('room', 'user', 'date', 'time', 'duration')
    list_filter = ('date', 'room')
    ordering = ('date', 'time')
