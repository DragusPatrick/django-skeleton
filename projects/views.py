from django.shortcuts import render
from django.views import generic
from .models import Project


class ProjectList(generic.ListView):
    queryset = Project.objects.filter(status=1).order_by('-created_on')
    template_name = 'project_list.html'


class ProjectDetail(generic.DetailView):
    model = Project
    template_name = 'project_detail.html'
