from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse

def is_admin(user):
    return user.is_superuser or user.is_staff

def is_teacher(user):
    return not user.is_superuser and not user.is_staff

def home(request):
    if request.user.is_authenticated:
        if is_admin(request.user):
            return redirect('admin_dashboard')
        else:
            return redirect('teacher_dashboard')
    return redirect('login')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if is_admin(user):
                return redirect('admin_dashboard')
            else:
                return redirect('teacher_dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def admin_dashboard(request):
    if not is_admin(request.user):
        return redirect('teacher_dashboard')
    
    context = {
        'user': request.user,
        'stats': {
            'total_teachers': 24,
            'total_subjects': 42,
            'total_files': 156,
        },
        'recent_files': [
            {
                'id': 1,
                'filename': 'Midterm_Exam_2023.pdf',
                'subject': 'Mathematics',
                'teacher': 'John Smith',
                'upload_date': 'Oct 12, 2023'
            },
            {
                'id': 2,
                'filename': 'Final_Exam_Questions.docx',
                'subject': 'Physics',
                'teacher': 'Sarah Johnson',
                'upload_date': 'Oct 10, 2023'
            },
        ]
    }
    return render(request, 'admin/dashboard.html', context)

@login_required
def teacher_dashboard(request):
    context = {
        'user': request.user,
        'my_files': [
            {
                'id': 1,
                'filename': 'Midterm_Exam_2023.pdf',
                'subject': 'Mathematics',
                'size': '2.4 MB',
                'upload_date': 'Oct 12, 2023'
            },
            {
                'id': 2,
                'filename': 'Quiz_Questions.docx',
                'subject': 'Physics',
                'size': '1.8 MB',
                'upload_date': 'Oct 5, 2023'
            },
        ]
    }
    return render(request, 'teacher/dashboard.html', context)

# Add other view functions
@login_required
def upload_file(request):
    return render(request, 'teacher/upload.html')

@login_required
def file_list(request):
    return render(request, 'file_list.html')

@login_required
def manage_departments(request):
    return render(request, 'admin/manage_departments.html')

@login_required
def manage_subjects(request):
    return render(request, 'admin/manage_subjects.html')

@login_required
def manage_teachers(request):
    return render(request, 'admin/manage_teachers.html')

@login_required
def manage_folders(request):
    return render(request, 'admin/manage_folders.html')

@login_required
def view_questionnaires(request):
    return render(request, 'admin/view_questionnaires.html')