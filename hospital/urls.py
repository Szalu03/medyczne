from django.urls import path
from hospital import views

urlpatterns = [
    path('', views.home, name='home'),
    path('rooms/', views.room_list, name='room_list'),
    path('reservations/', views.reservation_list, name='reservation_list'),
    path('reservations/new/', views.create_reservation, name='create_reservation'),
    path('reservations/<int:pk>/', views.reservation_detail, name='reservation_detail'),
    path('reservations/<int:pk>/delete/', views.delete_reservation, name='delete_reservation'),
    path('login/hospital/admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('make_reservation/', views.make_reservation, name='make_reservation'),
    path('login/', views.login_view, name='login')
]

