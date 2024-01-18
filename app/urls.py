from django.urls import path

from app.views import IndexView, TagListView, TaskCreateView

urlpatterns = [
    path("home/", IndexView.as_view(), name="index"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("tags/", TagListView.as_view(), name="tag-list"),
]

app_name = "app"
