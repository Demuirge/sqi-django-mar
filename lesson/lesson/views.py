from django.shortcuts import render, get_object_or_404

from .models import Department, Student

# Create your views here.

def home(request):
    return render(request, "lesson/home.html")

def students(request):
    all_students = Student.objects.all()
    return render(request, "lesson/students.html", {"all_students" : all_students})

def departments(request):
    all_departments = Department.objects.all()
    return render(request, "lesson/departments.html", {"all_departments": all_departments})

def student_detail(request, student_id):
    st_detail = get_object_or_404(Student, id=student_id)
    return render(request, "lesson/student_detail.html", {"st_detail": st_detail})

def department_detail(request, department_id):
    dept_detail = get_object_or_404(Department, id=department_id)
    return render(request, "lesson/department_detail.html", {"dept_detail": dept_detail})
