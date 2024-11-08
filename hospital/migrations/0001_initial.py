# Generated by Django 4.2.16 on 2024-11-08 16:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('room_type', models.CharField(choices=[('operacyjna', 'Sala Operacyjna'), ('zabiegowa', 'Sala Zabiegowa'), ('konsultacyjna', 'Sala Konsultacyjna')], max_length=20)),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('doctor', 'Doctor'), ('nurse', 'Nurse'), ('technician', 'Technician')], max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('duration', models.DurationField()),
                ('equipment', models.ManyToManyField(blank=True, to='hospital.equipment')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.room')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.staff')),
            ],
            options={
                'unique_together': {('room', 'date', 'time')},
            },
        ),
    ]
