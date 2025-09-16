from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_student, name='register_student'),
    path('success/', views.student_success, name='student_success'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-student/', views.add_student, name='add_student'),
    path('add-staff/', views.add_staff, name='add_staff'),
    path('mark-attendance/', views.mark_attendance, name='mark_attendance'),
    path('enter-grade/', views.enter_grade, name='enter_grade'),
    path('view-grades/', views.view_grades, name='view_grades'),
]