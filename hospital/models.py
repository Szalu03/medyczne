# hospital/models.py
from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    ROOM_TYPES = [
        ('operacyjna', 'Sala Operacyjna'),
        ('zabiegowa', 'Sala Zabiegowa'),
        ('konsultacyjna', 'Sala Konsultacyjna'),
    ]
    name = models.CharField(max_length=100)
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.get_room_type_display()})"


from django.db import models
from django.contrib.auth.models import User

class Staff(models.Model):
    ROLE_CHOICES = [
        ('doctor', 'Doctor'),
        ('technician', 'Technician'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.name} (Qty: {self.quantity})"






class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    duration = models.DurationField()
    created_at = models.DateTimeField(null=True, blank=True) # Only auto_now_add
    updated_at = models.DateTimeField(auto_now=True)
    field = models.DateTimeField(auto_now_add=True, default="2024-11-08 12:00:00"),

    def __str__(self):
        return f"Reservation for {self.room} by {self.user.username} on {self.date} at {self.time}"
