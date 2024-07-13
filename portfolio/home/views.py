from django.shortcuts import render, get_object_or_404
from .models import Project, Tag


# Create your views here.

def homepage(request):
    projects = Project.objects.all()
    tags = Tag.objects.all()
    context = {"projects": projects, "tags": tags}
    return render(request, "homepage.html", context)

def contact(request):
    return render(request, "contact.html")

def project(request, id):
    project = get_object_or_404(Project, pk=id)
    context = {"project":project}
    return render(request, "project.html", context)