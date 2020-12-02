from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib import messages
from .models import *
from .forms import *
from accounts.views import *
from accounts.models import *
from django.db.models import Q
from django.utils.timezone import datetime

from .decorators import allowed_users

# Create your views here.



@login_required(login_url='login')
def student(request):
    now = datetime.now()
    required = 0
    active = 0
    receptive = 0
    eventStudent = Event_Student.objects.all().filter(student_id=request.user.id)
    for i in eventStudent:
        hour = Event.objects.all().filter(id=i.Event_id)
        for j in hour:
            if j.type_hour == "Required":
                required += j.length
            if j.type_hour == "Active":
                active += j.length
            if j.type_hour == "Receptive":
                receptive += j.length
    sum = required + active + receptive
    Required_hour = required * 5
    Active_hour = active * 100 // 60
    Receptive_hour = receptive  * 5
    event = Event.objects.all()
    name = request.user.get_full_name()
    context = {'event':event, 'name': name, 'required':required, 'active':active,'receptive':receptive, 'sum':sum, 'Required_hour':
    Required_hour,'Active_hour':Active_hour,'Receptive_hour':Receptive_hour}
    return render(request, 'Student/index.html', context)

@login_required(login_url='login')
def student_table(request):
    eventStudent = Event_Student.objects.all().filter(student_id=request.user.id)
    name = request.user.get_full_name()
    context = {'eventStudent':eventStudent, 'name':name}
    return render(request, 'Student/table.html', context)

def student_required(request):
    student = Student.objects.all().filter(student_id=1)


@login_required(login_url='login')
def student_addHour(request):
    form = AddHourForm()
    if request.method == "POST":
        form = AddHourForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-home')
    name = request.user.get_full_name()
    context = {'form': form, 'name': name}
    return render(request, 'Student/Add hours.html', context)

def student_deleteHour(request, pk):
    hour = Event_Student.objects.get(id=pk)
    if request.method == "POST":
        hour.delete()
        return redirect('../student/table')
    context = {'item': hour}
    return render(request, 'Student/table.html', context)

@login_required(login_url='login')
def faculty(request):
    name = request.user.get_full_name()
    context = {'name': name}
    return render(request, 'Faculty/index.html', context)

@login_required(login_url='login')
def faculty_memebers(request):
    name = request.user.get_full_name()
    student = Student.objects.all().filter(faculty_id=1)
    total_student = student.count()
    return render(request, 'Faculty/members.html', {'student':student, 'total_student': total_student})

@login_required(login_url='login')
def faculty_table(request):
    name = request.user.get_full_name()
    event_student = Event_Student.objects.all().filter(Status="Pending")
    context={"event_student": event_student, 'name': name}
    return render(request, "Faculty/table.html", context)

@login_required(login_url='login')
def faculty_updateStatus(request, pk):
    hour = Event_Student.objects.get(id=pk)
    hour.Status="Approved"
    Event_Student.save(hour)
    context={'hour':hour}
    return render(request, "Faculty/table.html", context)

@login_required(login_url='login')
def faculty_denyHour(request, pk):
    hour = Event_Student.objects.get(id=pk)
    hour.Status="Denied"
    Event_Student.save(hour)
    context={'hour':hour}
    return render(request, "Faculty/table.html", context)

@login_required(login_url='login')
def monitor(request):
    name = request.user.get_full_name()
    context = {'name': name}
    return render(request, 'Monitor/index.html', context)

@login_required(login_url='login')
def monitor_archive_events(request):
    name = request.user.get_full_name()
    context = {'name': name}
    return render(request, 'Monitor/Archive_events.html', context)

@login_required(login_url='login')
def monitor_table(request):
    name = request.user.get_full_name()
    context = {'name': name}
    return render(request, 'Monitor/table.html', context)

@login_required(login_url='login')
def monitor_faculty_mem(request):
    name = request.user.get_full_name()
    faculty = Faculty.objects.all()

    total_faculty = faculty.count()
    context = {'faculty':faculty,'total_faculty':total_faculty,'name': name}
    return render(request, 'Monitor/Faculty members.html', context)

@login_required(login_url='login')
def monitor_student_mem(request):
    name = request.user.get_full_name()
    context = {'name': name}
    return render(request, 'Monitor/Student members.html', context)
