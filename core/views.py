from django.shortcuts import render, redirect
from .forms import StudentForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_success')
    else:
        form = StudentForm()
    return render(request, 'register_student.html', {'form': form})

from django.shortcuts import render

def student_success(request):
    return render(request, 'student_success.html')

from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    role = request.user.role
    if role == 'admin':
        return render(request, 'admin_dashboard.html')
    elif role == 'staff':
        return render(request, 'staff_dashboard.html')
    elif role == 'student':
        return render(request, 'student_dashboard.html')
    else:
        return redirect('login')
    
    from .forms import StudentForm, StaffForm

@login_required
def add_student(request):
    if request.user.role != 'admin':
        return redirect('dashboard')
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'add_student.html', {'form': form})

@login_required
def add_staff(request):
    if request.user.role != 'admin':
        return redirect('dashboard')
    form = StaffForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'add_staff.html', {'form': form})

@login_required
def mark_attendance(request):
    if request.user.role != 'staff':
        return redirect('dashboard')
    form = AttendanceForm(request.POST or None)
    if form.is_valid():
        attendance = form.save(commit=False)
        attendance.marked_by = request.user
        attendance.save()
        return redirect('dashboard')
    return render(request, 'mark_attendance.html', {'form': form})

@login_required
def enter_grade(request):
    if request.user.role != 'staff':
        return redirect('dashboard')
    form = GradeForm(request.POST or None)
    if form.is_valid():
        grade = form.save(commit=False)
        grade.graded_by = request.user
        grade.save()
        return redirect('dashboard')
    return render(request, 'enter_grade.html', {'form': form})

@login_required
def view_grades(request):
    if request.user.role == 'student':
        grades = Grade.objects.filter(student__email=request.user.email)
    elif request.user.role == 'staff':
        grades = Grade.objects.filter(graded_by=request.user)
    elif request.user.role == 'admin':
        grades = Grade.objects.all()
    else:
        grades = []
    return render(request, 'view_grades.html', {'grades': grades})