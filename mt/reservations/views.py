from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import Reservation
from .serializers import ReservationSerializer

class ReservationCreateView(generics.CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class ReservationDetailView(generics.RetrieveAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

@api_view(["GET"])
def user_reservations(request, user_id):
    reservations = Reservation.objects.filter(customer__id=user_id)
    serializer = ReservationSerializer(reservations, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def update_reservation_status(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    reservation.status = request.data.get("status", reservation.status)
    reservation.save()
    return Response({"message": "Status updated", "status": reservation.status})

@api_view(["DELETE"])
def delete_reservation(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    reservation.delete()
    return Response({"message": "Reservation deleted"})