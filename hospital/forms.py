# hospital/forms.py
from django import forms
from django.core.exceptions import ValidationError
from hospital.models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['room', 'date', 'time', 'duration']

    def clean(self):
        cleaned_data = super().clean()
        room = cleaned_data.get('room')
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')
        duration = cleaned_data.get('duration')

        # Check for overlapping reservations
        if Reservation.objects.filter(
            room=room,
            date=date,
            time__lte=(time + duration),
            time__gte=(time - duration)
        ).exists():
            raise ValidationError("This room is already reserved at the selected time.")
        return cleaned_data
