from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='login'),
    path('logout', views.logoutUser, name='logout'),

    path('student/', views.student, name='student-home'),
    path('student/table', views.student_table, name='student-table'),
    path('student/add_hour', views.student_addHour, name="student-addHour"),
    path('student/delete_hour/<str:pk>/', views.student_deleteHour, name="student-deleteHour"),

    path('faculty/', views.faculty, name='faculty-home'),
    path('faculty/members', views.faculty_memebers, name='faculty-memebers'),
    path('faculty/table', views.faculty_table, name='faculty-table'),
    path('faculty/update_status/<str:pk>/', views.faculty_updateStatus, name="faculty-updateStatus"),
    path('faculty/deny_hour/<str:pk>/', views.faculty_denyHour, name="faculty-denyHour"),

    path('monitor/', views.monitor, name='monitor-home'),
    path('monitor/archive_events', views.monitor_archive_events, name='monitor-archive_events'),
    path('monitor/table', views.monitor_table, name='monitor-table'),
    path('monitor/faculty_mem', views.monitor_faculty_mem, name='monitor-faculty_mem'),
    path('monitor/student_mem', views.monitor_student_mem, name='monitor-student_mem'),
]
