from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class Participant(AbstractUser):
    contact_number = models.CharField("Contact Number", max_length = 50)
    
    STUDENTS = 1
    FACULTY = 2
    STAFF = 3
    DESIGNATIONS = ((STUDENTS, 'Student'), (FACULTY, 'Faculty'), (STAFF, 'Staff'))
    designation = models.CharField("", max_length = 7, default="", choices=DESIGNATIONS)

    def __str__(self):
        return self.username
