# hospital/views.py
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

from hospital.forms import ReservationForm
from hospital.models import Room, Reservation


def home(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login if not authenticated
    return render(request, 'hospital/home.html')

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'hospital/room_list.html', {'rooms': rooms})

def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'hospital/reservation_list.html', {'reservations': reservations})

@login_required
def create_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            messages.success(request, "Reservation created successfully.")
            return redirect('hospital:reservation_list')
    else:
        form = ReservationForm()
    return render(request, 'hospital/create_reservation.html', {'form': form})

@login_required
def reservation_detail(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    return render(request, 'hospital/reservation_detail.html', {'reservation': reservation})

@login_required
@user_passes_test(lambda u: u.is_staff)
def delete_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    reservation.delete()
    messages.success(request, "Reservation deleted successfully.")
    return redirect('hospital:reservation_list')


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from hospital.models import Staff
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        # Debug output
        print(f"Authenticating user: {username}")

        if user is not None:  # Check if the user exists
            login(request, user)
            print(f"User '{username}' logged in successfully.")

            try:
                # Check the user’s role in the Staff model
                staff = user.staff
                print(f"User role: {staff.role}")  # Debug output for user role

                if staff.role == 'technician':
                    print("Redirecting to admin dashboard")
                    return redirect('hospital/admin_dashboard')  # Redirect to the admin dashboard
                elif staff.role == 'doctor':
                    print("Redirecting to home page")
                    return redirect('/')  # Redirect to home for doctors
            except Staff.DoesNotExist:
                print("User has no specific role, redirecting to home.")
                return redirect('/')  # Default redirect if no specific role exists

        else:
            messages.error(request, "Invalid username or password.")
            print("Authentication failed.")

    return render(request, 'hospital/login.html')


@login_required
@user_passes_test(lambda u: u.is_staff)
def admin_dashboard(request):
    return render(request, 'hospital/admin_dashboard.html')

@login_required
def user_dashboard(request):
    rooms = Room.objects.all()
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'hospital/user_dashboard.html', {'rooms': rooms, 'reservations': reservations})

@login_required
def make_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            messages.success(request, "Reservation made successfully!")
            return redirect('hospital:user_dashboard')
    else:
        form = ReservationForm()
    return render(request, 'hospital/make_reservation.html', {'form': form})
