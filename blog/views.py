from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Blog


# Create your views here.
def index(request):
    context = {"blogs": Blog.objects.filter(is_home=True, is_active=True)}
    return render(request, "blog/index.html", context)


def blogs(request):
    context = {"blogs": Blog.objects.filter(is_home=True)}
    return render(request, "blog/blogs.html", context)


def blog_details(request, id):
    blog = Blog.objects.get(id=id)
    return render(request, "blog/blog-details.html", {"blog": blog})
