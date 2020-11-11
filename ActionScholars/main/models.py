from django.db import models

# Create your models here.
class Monitor(models.Model):
    username = None
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length = 254, unique=True)
    password = models.CharField(null=True, max_length=100)
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.first_name

class Faculty(models.Model):
    username = None
    Status = (
        ("Active", "Active"),
        ("inactive", "inactive"),
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length = 254, unique=True)
    password = models.CharField(null=True, max_length=100)
    status = models.CharField(max_length=30, null=True, choices=Status)
    year = models.CharField(null=True, max_length=100)
    USERNAME_FIELD = 'email'


    def __str__(self):
        return self.first_name


class Monitor_Faculty(models.Model):
    monitor = models.ForeignKey(to=Monitor, on_delete=models.CASCADE)
    faculty = models.ForeignKey(to=Faculty, on_delete=models.CASCADE)

class Student(models.Model):
    username = None
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length = 254, unique=True)
    password = models.CharField(null=True, max_length=100)
    required_hour = models.FloatField(null=True)
    receptive_hour = models.FloatField(null=True)
    active_hour = models.FloatField(null=True)
    faculty = models.ForeignKey(to=Faculty, null=True,on_delete=models.CASCADE)
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.first_name

class Event(models.Model):
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
    TypeHours = (
        ("Required", "Required"),
        ("Active", "Active"),
        ("Receptive", "Receptive"),
    )
    student = models.ForeignKey(to=Student, on_delete=models.CASCADE)
    Event = models.ForeignKey(to=Event, on_delete=models.CASCADE)
    Status = models.CharField(max_length=30, null = False, default="Pending",choices=Status)
    Student_Reflection = models.CharField(max_length=300)

    def __str__(self):
        return self.student
