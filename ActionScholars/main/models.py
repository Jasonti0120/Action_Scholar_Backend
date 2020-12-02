from django.db import models
from accounts.models import *

# Create your models here.


class Event(models.Model):
    TypeHours = (
        ("Required", "Required"),
        ("Active", "Active"),
        ("Receptive", "Receptive"),
    )
    name = models.CharField(max_length=30)
    date = models.DateTimeField()
    description = models.CharField(max_length=300)
    length = models.FloatField()
    type_hour = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Event_Student(models.Model):
    Status = (
        ("Approved", "Approved"),
        ("Pending", "Pending"),
        ("Denied", "Denied"),
    )
    student = models.ForeignKey(to=User, on_delete=models.CASCADE)
    Event = models.ForeignKey(to=Event, on_delete=models.CASCADE)
    Status = models.CharField(max_length=30, null = False, default="Pending",choices=Status)
    Student_Reflection = models.CharField(max_length=300, null = True)

    def __str__(self):
        return self.student
