from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    course = models.CharField(max_length=100)
    join_date = models.DateField()

class Staff(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    email = models.EmailField()

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('student', 'Student'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')])
    marked_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # staff user

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    marks = models.IntegerField()
    graded_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # staff user
    date_recorded = models.DateField(auto_now_add=True)