from django.urls import path
from ..reservations.views import TableListCreateView, available_tables

urlpatterns = [
    path("", TableListCreateView.as_view(), name="table-list"),
    path("available/", available_tables, name="available-tables"),
]