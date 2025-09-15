from django.contrib import admin
from .models import Student, Staff, Course
from .models import CustomUser

admin.site.register(CustomUser)
admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(Course)