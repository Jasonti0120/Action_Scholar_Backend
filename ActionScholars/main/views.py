from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *
from django.db.models import Q
from django.utils.timezone import datetime



# Create your views here.
def home(request):
    e = request.POST.get('email')
    pas = request.POST.get('password')
    if Student.objects.filter(email = e).filter(password=pas):
        return redirect('student-home')

    if Faculty.objects.filter(email = e).filter(password=pas):
        return redirect('faculty-home')

    if Monitor.objects.filter(email = e).filter(password=pas):
        return redirect('monitor-home')
    else:
	       messages.info(request, 'Username OR password is incorrect')
    return render(request, 'login/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

# @login_required(login_url='login')
def student(request):
    now = datetime.now()
    event = Event.objects.all()
    return render(request, 'Student/index.html', {'event':event})

# @login_required(login_url='login')
def student_table(request):
    eventStudent = Event_Student.objects.all().filter(student_id=1)
    return render(request, 'Student/table.html', {'eventStudent':eventStudent})

def student_required(request):
    student = Student.objects.all().filter(student_id=1)
    

# @login_required(login_url='login')
def student_addHour(request):
    form = AddHourForm()
    if request.method == "POST":
        form = AddHourForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-home')
    context = {'form': form}
    return render(request, 'Student/Add hours.html', context)

def student_deleteHour(request, pk):
    hour = Event_Student.objects.get(id=pk)
    if request.method == "POST":
        hour.delete()
        return redirect('../student/table')
    context = {'item': hour}
    return render(request, 'Student/table.html', context)

# @login_required(login_url='login')
def faculty(request):
    return render(request, 'Faculty/index.html')

# @login_required(login_url='login')
def faculty_memebers(request):
    student = Student.objects.all().filter(faculty_id=1)

    total_student = student.count()
    return render(request, 'Faculty/members.html', {'student':student, 'total_student': total_student})

# @login_required(login_url='login')
def faculty_table(request):
    event_student = Event_Student.objects.all().filter(Status="Pending")
    context={"event_student": event_student}
    return render(request, "Faculty/table.html", context)

def faculty_updateStatus(request, pk):
    hour = Event_Student.objects.get(id=pk)
    hour.Status="Approved"
    Event_Student.save(hour)
    context={'hour':hour}
    return render(request, "Faculty/table.html", context)

def faculty_denyHour(request, pk):
    hour = Event_Student.objects.get(id=pk)
    hour.Status="Denied"
    Event_Student.save(hour)
    context={'hour':hour}
    return render(request, "Faculty/table.html", context)

# @login_required(login_url='login')
def monitor(request):
    return render(request, 'Monitor/index.html')

# @login_required(login_url='login')
def monitor_archive_events(request):
    return render(request, 'Monitor/Archive_events.html')

# @login_required(login_url='login')
def monitor_table(request):
    return render(request, 'Monitor/table.html')

# @login_required(login_url='login')
def monitor_faculty_mem(request):
    faculty = Faculty.objects.all()

    total_faculty = faculty.count()
    return render(request, 'Monitor/Faculty members.html', {'faculty':faculty,'total_faculty':total_faculty})

# @login_required(login_url='login')
def monitor_student_mem(request):
    return render(request, 'Monitor/Student members.html')
