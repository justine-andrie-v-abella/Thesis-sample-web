from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Admin URLs
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/departments/', views.manage_departments, name='manage_departments'),
    path('admin/subjects/', views.manage_subjects, name='manage_subjects'),
    path('admin/teachers/', views.manage_teachers, name='manage_teachers'),
    path('admin/folders/', views.manage_folders, name='manage_folders'),
    path('admin/questionnaires/', views.view_questionnaires, name='view_questionnaires'),
    
    # Teacher URLs
    path('teacher/dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('teacher/upload/', views.upload_file, name='upload_file'),
    
    # File operations
    path('files/', views.file_list, name='file_list'),
    path('files/<int:file_id>/download/', views.download_file, name='download_file'),
    path('files/<int:file_id>/view/', views.view_file, name='view_file'),
    path('files/<int:file_id>/delete/', views.delete_file, name='delete_file'),
]