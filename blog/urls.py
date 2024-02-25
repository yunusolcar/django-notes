from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="homepage"),
    path("index", views.index),
    path("blogs", views.blogs, name="blogs"),
    path("blogs/<slug:slug>", views.blog_details, name="blog_details"),
]
