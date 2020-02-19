from django.shortcuts import render
from projects.models import Project


def homepage(request):
    all_projects = Project.objects.filter(status=1).order_by('-created_on')

    context = {
        "all_projects": all_projects
    }

    return render(request, 'pages/homepage.html', context)


def about(request):
    return render(request, 'pages/about.html')