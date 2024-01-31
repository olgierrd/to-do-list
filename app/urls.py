from django.urls import path

from app.views import IndexView, TagListView, TaskCreateView, TaskStatusUpdateView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/complete/", TaskStatusUpdateView.as_view(), name="task-complete-undo"),
    path("tags/", TagListView.as_view(), name="tag-list"),
]

app_name = "app"
