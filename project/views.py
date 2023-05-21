from django.shortcuts import render
from .models import Project
# Create your views here.

def proje(request):
    project = Project.objects.all()
    context = {
        'project':project
    }
    return render(request, 'portfolio/proje.html', context)
