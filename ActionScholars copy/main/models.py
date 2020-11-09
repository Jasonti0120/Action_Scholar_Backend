from django.db import models

# Create your models here.
class Admin(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length = 254)

class Faculty(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length = 254)
    grade = models.CharField(max_length=30)

class Admin_Faculty(models.Model):
    admin = models.ForeignKey(to=Admin, on_delete=models.CASCADE)
    faculty = models.ForeignKey(to=Faculty, on_delete=models.CASCADE)

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length = 254)
    grade = models.CharField(max_length=30)
    required_hour = models.FloatField()
    receptive_hour = models.FloatField()
    active_hour = models.FloatField()
    faculty = models.ForeignKey(to=Faculty, on_delete=models.CASCADE)

class Event(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateTimeField()
    description = models.CharField(max_length=300)
    length = models.FloatField()
    type_hour = models.CharField(max_length=30)

class Event_Student(models.Model):
    Status = (
        ("Approved", "Approved"),
        ("Pending", "Pending"),
        ("Denied", "Denied"),
    )
    TypeHours = (
        ("Required", "Required"),
        ("Active", "Active"),
        ("Receptive", "Receptive"),
    )
    student = models.ForeignKey(to=Student, on_delete=models.CASCADE)
    Event = models.ForeignKey(to=Event, on_delete=models.CASCADE)
    Status = models.CharField(max_length=30, null = True, choices=Status)
    Hours = models.CharField(max_length=30, null = True, choices=TypeHours)
    Student_Reflection = models.CharField(max_length=300)
