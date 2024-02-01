from django.urls import reverse_lazy
from django.views import generic

from app.forms import TaskForm, TagForm
from app.models import Task, Tag


class IndexView(generic.ListView):
    model = Task
    template_name = "app/index.html"
    context = {"tasks": Task.objects.all()}


class TagListView(generic.ListView):
    model = Tag
    template_name = "app/tag_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    template_name = "app/tag_form.html"
    success_url = reverse_lazy("app:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("app:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("app:tag-list")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "app/task_form.html"
    success_url = reverse_lazy("app:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("app:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("app:index")


class TaskStatusUpdateView(generic.UpdateView):
    model = Task
    fields = ["done"]
    success_url = reverse_lazy("app:index")
