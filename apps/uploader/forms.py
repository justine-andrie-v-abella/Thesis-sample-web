from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ["title", "file"]

    def clean_file(self):
        file = self.cleaned_data.get("file")
        valid_extensions = [".csv", ".xlsx", ".docx"]
        if not any(file.name.endswith(ext) for ext in valid_extensions):
            raise forms.ValidationError("Only CSV, Excel (.xlsx), and Word (.docx) files are allowed.")
        return file
