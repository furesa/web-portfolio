from django.shortcuts import render
from projects.models import Project, Cheatsheet


# Create your views here.
def project_index(request):
    projects = Project.objects.all()
    cheatsheets = Cheatsheet.objects.all()
    context = {
        'projects': projects,
        'cheatsheets': cheatsheets
    }
    return render(request, 'project_index.html', context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)


def cheatsheet_detail(request, pk):
    cheatsheet = Cheatsheet.objects.get(pk=pk)
    context = {
        'cheatsheet': cheatsheet
    }
    return render(request, 'cheatsheet_detail.html', context)
