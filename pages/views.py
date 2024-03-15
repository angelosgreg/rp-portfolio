# pages/views.py

from django.shortcuts import render

def home(request):
    return render(request, "pages/home.html", {})
# projects/views.py

from projects.models import Project

def project_index(request):
    projects = Project.objects.all()
    context = {
        "projects": projects
    }
    return render(request, "projects/project_index.html", context)
