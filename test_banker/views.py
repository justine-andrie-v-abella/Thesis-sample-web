from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
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
    if request.user.is_authenticated:
        if is_admin(request.user):
            return redirect('admin_dashboard')
        else:
            return redirect('teacher_dashboard')
            
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
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('login')

@login_required
def admin_dashboard(request):
    if not is_admin(request.user):
        return redirect('teacher_dashboard')
    
    # Sample data - replace with your actual data
    context = {
        'user': {
            'name': request.user.get_full_name() or request.user.username,
            'email': request.user.email,
            'initials': (request.user.get_full_name() or request.user.username)[:2].upper()
        },
        'teachers_count': 42,
        'subjects_count': 24,
        'files_count': 1248,
        'recent_activities': [
            {
                'teacher': {
                    'initials': 'JD', 
                    'name': 'John Doe', 
                    'email': 'johndoe@example.com'
                },
                'subject': 'Mathematics',
                'filename': 'Algebra_Quiz_1.pdf',
                'size': '2.4 MB',
                'date': 'May 15, 2023'
            },
            {
                'teacher': {
                    'initials': 'SJ', 
                    'name': 'Sarah Johnson', 
                    'email': 'sjohnson@example.com'
                },
                'subject': 'Physics',
                'filename': 'Mechanics_Test.pdf',
                'size': '3.1 MB',
                'date': 'May 14, 2023'
            },
        ]
    }
    return render(request, 'admin/dashboard.html', context)

@login_required
def teacher_dashboard(request):
    # Sample data - replace with your actual data
    context = {
        'user': {
            'name': request.user.get_full_name() or request.user.username,
            'email': request.user.email,
            'initials': (request.user.get_full_name() or request.user.username)[:2].upper()
        },
        'assigned_subjects': [
            {'id': 1, 'name': 'Mathematics'},
            {'id': 2, 'name': 'Physics'},
            {'id': 3, 'name': 'Chemistry'},
        ],
        'uploaded_files': [
            {
                'id': 1,
                'filename': 'Algebra_Quiz_1.pdf',
                'subject': 'Mathematics',
                'size': '2.4 MB',
                'upload_date': 'May 15, 2023'
            },
            {
                'id': 2,
                'filename': 'Geometry_Test.docx',
                'subject': 'Mathematics',
                'size': '1.8 MB',
                'upload_date': 'May 10, 2023'
            },
        ]
    }
    return render(request, 'teacher/dashboard.html', context)

@login_required
def upload_file(request):
    if not is_teacher(request.user):
        return redirect('admin_dashboard')
    
    if request.method == 'POST':
        # Handle file upload logic here
        subject_id = request.POST.get('subject')
        file = request.FILES.get('file')
        description = request.POST.get('description')
        
        # Add your file processing logic here
        messages.success(request, 'File uploaded successfully!')
        return redirect('teacher_dashboard')
    
    context = {
        'user': {
            'name': request.user.get_full_name() or request.user.username,
            'email': request.user.email,
            'initials': (request.user.get_full_name() or request.user.username)[:2].upper()
        },
        'assigned_subjects': [
            {'id': 1, 'name': 'Mathematics'},
            {'id': 2, 'name': 'Physics'},
            {'id': 3, 'name': 'Chemistry'},
        ]
    }
    return render(request, 'teacher/upload.html', context)

@login_required
def file_list(request):
    context = {
        'user': {
            'name': request.user.get_full_name() or request.user.username,
            'email': request.user.email,
            'initials': (request.user.get_full_name() or request.user.username)[:2].upper()
        },
        'files': [
            {
                'id': 1,
                'filename': 'Algebra_Quiz_1.pdf',
                'subject': 'Mathematics',
                'teacher': 'John Doe',
                'size': '2.4 MB',
                'upload_date': 'May 15, 2023'
            },
            # Add more files...
        ]
    }
    return render(request, 'file_list.html', context)

@login_required
def manage_departments(request):
    if not is_admin(request.user):
        return redirect('teacher_dashboard')
    
    context = {
        'user': {
            'name': request.user.get_full_name() or request.user.username,
            'email': request.user.email,
            'initials': (request.user.get_full_name() or request.user.username)[:2].upper()
        },
        'departments': [
            {'id': 1, 'name': 'Mathematics', 'teacher_count': 5},
            {'id': 2, 'name': 'Science', 'teacher_count': 8},
            {'id': 3, 'name': 'Languages', 'teacher_count': 6},
        ]
    }
    return render(request, 'admin/manage_departments.html', context)

@login_required
def manage_subjects(request):
    if not is_admin(request.user):
        return redirect('teacher_dashboard')
    
    context = {
        'user': {
            'name': request.user.get_full_name() or request.user.username,
            'email': request.user.email,
            'initials': (request.user.get_full_name() or request.user.username)[:2].upper()
        },
        'subjects': [
            {'id': 1, 'name': 'Algebra', 'department': 'Mathematics'},
            {'id': 2, 'name': 'Geometry', 'department': 'Mathematics'},
            {'id': 3, 'name': 'Physics', 'department': 'Science'},
        ]
    }
    return render(request, 'admin/manage_subjects.html', context)

@login_required
def manage_teachers(request):
    if not is_admin(request.user):
        return redirect('teacher_dashboard')
    
    context = {
        'user': {
            'name': request.user.get_full_name() or request.user.username,
            'email': request.user.email,
            'initials': (request.user.get_full_name() or request.user.username)[:2].upper()
        },
        'teachers': [
            {
                'id': 1, 
                'name': 'John Doe', 
                'email': 'johndoe@example.com',
                'subjects': ['Mathematics', 'Physics'],
                'department': 'Science'
            },
            {
                'id': 2, 
                'name': 'Sarah Johnson', 
                'email': 'sjohnson@example.com',
                'subjects': ['Chemistry'],
                'department': 'Science'
            },
        ]
    }
    return render(request, 'admin/manage_teachers.html', context)

@login_required
def manage_folders(request):
    if not is_admin(request.user):
        return redirect('teacher_dashboard')
    
    context = {
        'user': {
            'name': request.user.get_full_name() or request.user.username,
            'email': request.user.email,
            'initials': (request.user.get_full_name() or request.user.username)[:2].upper()
        },
        'folders': [
            {'id': 1, 'name': 'Midterm Exams', 'subject': 'Mathematics', 'file_count': 15},
            {'id': 2, 'name': 'Final Exams', 'subject': 'Physics', 'file_count': 8},
            {'id': 3, 'name': 'Quizzes', 'subject': 'Chemistry', 'file_count': 12},
        ]
    }
    return render(request, 'admin/manage_folders.html', context)

@login_required
def view_questionnaires(request):
    if not is_admin(request.user):
        return redirect('teacher_dashboard')
    
    context = {
        'user': {
            'name': request.user.get_full_name() or request.user.username,
            'email': request.user.email,
            'initials': (request.user.get_full_name() or request.user.username)[:2].upper()
        },
        'questionnaires': [
            {
                'id': 1,
                'filename': 'Algebra_Midterm_2023.pdf',
                'subject': 'Mathematics',
                'teacher': 'John Doe',
                'folder': 'Midterm Exams',
                'size': '2.4 MB',
                'upload_date': 'May 15, 2023',
                'description': 'Midterm examination for Algebra course'
            },
            {
                'id': 2,
                'filename': 'Physics_Final_2023.docx',
                'subject': 'Physics',
                'teacher': 'Sarah Johnson',
                'folder': 'Final Exams',
                'size': '3.1 MB',
                'upload_date': 'May 14, 2023',
                'description': 'Final examination questions for Physics'
            },
        ]
    }
    return render(request, 'admin/view_questionnaires.html', context)

# Additional view functions for file operations
@login_required
def download_file(request, file_id):
    # Add your file download logic here
    # This is a placeholder - implement actual file download
    messages.success(request, 'File download started.')
    return redirect(request.META.get('HTTP_REFERER', 'teacher_dashboard'))

@login_required
def view_file(request, file_id):
    # Add your file viewing logic here
    # This is a placeholder - implement actual file viewing
    context = {
        'user': {
            'name': request.user.get_full_name() or request.user.username,
            'email': request.user.email,
            'initials': (request.user.get_full_name() or request.user.username)[:2].upper()
        },
        'file': {
            'id': file_id,
            'filename': 'Sample_File.pdf',
            'subject': 'Mathematics',
            'upload_date': 'May 15, 2023',
            'description': 'Sample file description'
        }
    }
    return render(request, 'file_preview.html', context)

@login_required
def delete_file(request, file_id):
    if request.method == 'POST':
        # Add your file deletion logic here
        messages.success(request, 'File deleted successfully.')
        if is_admin(request.user):
            return redirect('view_questionnaires')
        else:
            return redirect('teacher_dashboard')
    
    # If not POST, show confirmation page
    context = {
        'user': {
            'name': request.user.get_full_name() or request.user.username,
            'email': request.user.email,
            'initials': (request.user.get_full_name() or request.user.username)[:2].upper()
        },
        'file_id': file_id
    }
    return render(request, 'confirm_delete.html', context)