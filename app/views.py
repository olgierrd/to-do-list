from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

from app.models import Task, Tag


class IndexView(generic.TemplateView):
    model = Task
    template_name = "app/index.html"


class TagListView(generic.ListView):
    model = Tag



