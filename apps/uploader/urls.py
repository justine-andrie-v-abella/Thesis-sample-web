from django.urls import path
from . import views

app_name="uploader"
urlpatterns = [
    path("upload/", views.upload_file, name="upload_file"),
    path("files/", views.file_list, name="file_list"),
    path("files/<int:doc_id>/view/", views.view_file, name="view_file"),
    path("files/<int:doc_id>/download/", views.download_file, name="download_file"),
]
