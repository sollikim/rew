from django.db import models

# Create your models here.
class Table(models.Model):
    number = models.IntegerField(unique=True)
    seats = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Table {self.number} ({'Available' if self.is_available else 'Occupied'})"