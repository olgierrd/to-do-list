from django.urls import path

from app.views import IndexView, TagListView

urlpatterns = [
    path("home/", IndexView.as_view(), name="index"),
    path("tags/", TagListView.as_view(), name="tag-list"),
]

app_name = "app"
