# pages/models.py
from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    # You can add more fields as needed (e.g., slug, date, etc.)

    def __str__(self):
        return self.name

class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='images'
    )
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='project_images/')

    def __str__(self):
        return self.title