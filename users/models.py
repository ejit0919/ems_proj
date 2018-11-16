from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class Participant(AbstractUser):
    contact_number = models.CharField("Contact Number", max_length = 50)
    
    BLANK = 1
    STUDENTS = 2
    FACULTY = 3
    STAFF = 4
    DESIGNATIONS = ((BLANK, '-------'), (STUDENTS, 'Student'), (FACULTY, 'Faculty'), (STAFF, 'Staff'))
    designation = models.IntegerField("Designation", default="", choices=DESIGNATIONS)

    def __str__(self):
        return self.username
