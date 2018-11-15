from django.db import models
from django.urls import reverse

# Create your models here.

class Attendance(models.Model):
    for_date = models.TimeField("For Date")
    time_arrived = models.TimeField("Time Arrived")
    time_left = models.TimeField("Time Left")
    security_key = models.CharField("Security Key", max_length=8, default="")

    registration_id = models.ForeignKey(to="registrations.Registration", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("event_detail", args=[str(self.pk)])