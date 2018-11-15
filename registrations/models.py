from django.db import models
from django.urls import reverse

# Create your models here.

class Registration(models.Model):
    event = models.ForeignKey(to="events.Event", on_delete=models.CASCADE)
    participant = models.ForeignKey(to="users.Participant", on_delete=models.CASCADE)
    date_registered = models.DateTimeField("Date Registered", auto_now_add=True)
    parents_permit = models.FileField("Parents Permit", upload_to="reg/", default="")
    waiver = models.FileField("Waiver", upload_to="reg/", default="")
    parents_contact_number = models.CharField("Parent's Contact Number", max_length=50)

    status = models.CharField("Status", max_length=11, default="Pending")


    def __str__(self):
        return "{}-{}".format(self.event, self.participant)

    def get_absolute_url(self):
        return reverse("activities")