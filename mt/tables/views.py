from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from django.shortcuts import get_list_or_404
from .models import Table
from .serializers import TableSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

class TableListCreateView(generics.ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

@api_view(["GET"])
def available_tables(request):
    available = Table.objects.filter(is_available=True)
    serializer = TableSerializer(available, many=True)
    return Response(serializer.data)