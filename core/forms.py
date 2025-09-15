from django import forms
from .models import Student,Staff

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'course', 'join_date']

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['name', 'email', 'department']
from .models import Attendance

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'date', 'status']

from .models import Grade

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['student', 'subject', 'marks']