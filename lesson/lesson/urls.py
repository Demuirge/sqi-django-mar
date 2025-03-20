from django.urls import path

from . import views

app_name = "lesson"

urlpatterns = [
    path('', views.home, name="home"),
    path('students/', views.students, name="students"),
    path('departments/', views.departments, name="departments"),
    path('student_detail/<int:student_id>', views.student_detail, name="student_detail"),
    path('department_detail/<int:department_id>', views.department_detail, name="department_detail"),
]