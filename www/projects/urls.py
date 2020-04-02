from django.urls import path
from . import views


urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("<int:pk>/projects", views.project_detail, name="project_detail"),
    path("<int:pk>/cheatsheet/", views.cheatsheet_detail, name="cheatsheet_detail"),
]