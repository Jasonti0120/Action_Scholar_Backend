from django.shortcuts import render
from django.http import HttpResponse
# from django.http import HTTPResponse

# Create your views here.
def home(request):
    return render(request, 'login/login.html')

def student(request):
    return render(request, 'Student/index.html')

def student_table(request):
    return render(request, 'Student/table.html')

def student_addHour(request):
    return render(request, 'Student/Add hours.html')

def faculty(request):
    return render(request, 'Faculty/index.html')

def faculty_memebers(request):
    return render(request, 'Faculty/members.html')

def faculty_table(request):
    return render(request, "Faculty/table.html")


# def get_RequiredHoursByEmail(reqeust, semail):
#     if request.method == 'GET':
#         try:
#             student = Student.objects.get(email = semail)
#             return student.required_hour
#         except:
#             response = json.dumps([{ 'Error': 'No Student found'}])
#         return HttpResponse(response, content_type='text/json')
