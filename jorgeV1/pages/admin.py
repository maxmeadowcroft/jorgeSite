# pages/admin.py
from django.contrib import admin
from .models import Project, ProjectImage

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'image')
    list_filter = ('project',)
    search_fields = ('title', 'description')
