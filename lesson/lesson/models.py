from django.db import models

# Create your models here.
class Department(models.Model):
    department = models.CharField(max_length=255)
    no_of_students = models.PositiveIntegerField()

    def __str__(self):
        return self.department

class Student(models.Model):
    full_name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    birth_date = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name

