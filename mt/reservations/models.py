from django.db import models

# Create your models here.
class Reservation(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("canceled", "Canceled"),
    ]

    customer = models.ForeignKey("customers.Customer", on_delete=models.CASCADE)
    table = models.ForeignKey("tables.Table", on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")

    def __str__(self):
        return f"Reservation {self.id} - {self.customer.name} on {self.date}"