import csv
import openpyxl
import docx
import os
from django.shortcuts import render, redirect
from django.http import FileResponse, HttpResponse, Http404
from django.conf import settings
from .forms import DocumentForm
from .models import Document, Teacher


def upload_file(request):
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            doc = form.save()  # saves file to media/uploads/
            file_path = doc.file.path

            # CSV handling
            if file_path.endswith(".csv"):
                with open(file_path, newline="") as f:
                    reader = csv.reader(f)
                    next(reader, None)  # skip header if exists
                    for row in reader:
                        if len(row) >= 2:
                            Teacher.objects.create(name=row[0], age=int(row[1]))

            # Excel handling
            elif file_path.endswith(".xlsx"):
                wb = openpyxl.load_workbook(file_path)
                sheet = wb.active
                for i, row in enumerate(sheet.iter_rows(values_only=True)):
                    if i == 0:  # skip header
                        continue
                    if row and len(row) >= 2:
                        Teacher.objects.create(name=row[0], age=int(row[1]))

            # Word handling
            elif file_path.endswith(".docx"):
                docx_file = docx.Document(file_path)
                for para in docx_file.paragraphs:
                    parts = para.text.split(",")
                    if len(parts) >= 2:
                        try:
                            Teacher.objects.create(
                                name=parts[0].strip(), age=int(parts[1].strip())
                            )
                        except ValueError:
                            pass  # ignore invalid lines

            return redirect("uploader:file_list")
    else:
        form = DocumentForm()
    return render(request, "uploader/upload.html", {"form": form})


def file_list(request):
    documents = Document.objects.all()
    students = Teacher.objects.all()
    return render(
        request,
        "uploader/file_list.html",
        {"documents": documents, "students": students},
    )


def view_file(request, doc_id):
    """Open file inline (if browser supports it, e.g. PDF)."""
    try:
        doc = Document.objects.get(id=doc_id)
        file_path = doc.file.path
        if not os.path.exists(file_path):
            raise Http404("File not found")
        return FileResponse(open(file_path, "rb"), content_type="application/octet-stream")
    except Document.DoesNotExist:
        raise Http404("Document does not exist")


def download_file(request, doc_id):
    """Force download of the file."""
    try:
        doc = Document.objects.get(id=doc_id)
        file_path = doc.file.path
        if not os.path.exists(file_path):
            raise Http404("File not found")
        with open(file_path, "rb") as f:
            response = HttpResponse(f.read(), content_type="application/octet-stream")
            response["Content-Disposition"] = f'attachment; filename="{os.path.basename(file_path)}"'
            return response
    except Document.DoesNotExist:
        raise Http404("Document does not exist")
