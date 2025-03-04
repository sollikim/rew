from django.urls import path
from ..customers.views import (
    ReservationCreateView,
    ReservationDetailView,
    user_reservations,
    update_reservation_status,
    delete_reservation,
)

urlpatterns = [
    path("", ReservationCreateView.as_view(), name="reservation-create"),
    path("<int:pk>/", ReservationDetailView.as_view(), name="reservation-detail"),
    path("user/<int:user_id>/", user_reservations, name="user-reservations"),
    path("<int:id>/status/", update_reservation_status, name="update-reservation"),
    path("<int:id>/delete/", delete_reservation, name="delete-reservation"),
]