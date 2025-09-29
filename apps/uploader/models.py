from django.db import models

# stores the uploaded file
class Document(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to="uploads/")

    def __str__(self):
        return self.title

# example model for a teacher
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name
