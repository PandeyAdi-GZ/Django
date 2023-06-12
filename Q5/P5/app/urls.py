from django.urls import path
from . import views

urlpatterns = [
    path("", views.base, name = "base"),
    path("c1/", views.child1, name = "child1"),
    path("c2/", views.child2, name = "child2"),
]
