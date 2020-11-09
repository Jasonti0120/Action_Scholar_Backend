from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='login-home'),

    path('student/', views.student, name='student-home'),
    path('student/table', views.student_table, name='student-table'),
    path('student/add_hour', views.student_addHour, name="student-addHour"),

    path('faculty', views.faculty, name='faculty-home'),
    path('faculty/memebers', views.faculty_memebers, name='faculty-memebers'),
    path('faculty/table', views.faculty_table, name='faculty-table'),
]
