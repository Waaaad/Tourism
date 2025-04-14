from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    event = models.CharField(max_length=100)
    event_title = models.CharField(max_length=100)
    event_id = models.CharField(max_length=50)
    date = models.DateField()
    event_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # تأكد من إضافة هذا السطر

    def __str__(self):
        return f"{self.name} - {self.event_title}"