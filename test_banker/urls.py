"""
URL configuration for test_banker project.
"""

from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    # Put our custom URLs BEFORE the admin URLs
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Dashboards
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('teacher-dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    
    # File Operations
    path('upload/', views.upload_file, name='upload_file'),
    path('files/', views.file_list, name='file_list'),
    
    # Management (Admin only)
    path('manage/departments/', views.manage_departments, name='manage_departments'),
    path('manage/subjects/', views.manage_subjects, name='manage_subjects'),
    path('manage/teachers/', views.manage_teachers, name='manage_teachers'),
    path('manage/folders/', views.manage_folders, name='manage_folders'),
    path('manage/questionnaires/', views.view_questionnaires, name='view_questionnaires'),
    
    # Django admin - put this LAST
    path("django-admin/", admin.site.urls),  # Changed from 'admin/' to avoid conflict
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)