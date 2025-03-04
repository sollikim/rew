from rest_framework import serializers
from ..reservations.models import Table

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = "__all__"