from django.http import HttpResponse
from django.shortcuts import render


data = {
    "blogs": [
        {
            "id": 1,
            "title": "Javascript for Web Development",
            "image": "js.jpeg",
            "description": "Best JS Course",
            "is_active": True,
            "is_home": True,
        },
        {
            "id": 2,
            "title": "Python for ML",
            "image": "python.jpeg",
            "description": "Python for Beginners",
            "is_active": True,
            "is_home": True,
        },
        {
            "id": 3,
            "title": "React for Frontend Development",
            "image": "react.jpeg",
            "description": "React for Frontend Development",
            "is_active": False,
            "is_home": False,
        },
    ]
}


# Create your views here.
def index(request):
    context = {"blogs": data["blogs"]}
    return render(request, "blog/index.html", context)


def blogs(request):
    context = {"blogs": data["blogs"]}
    return render(request, "blog/blogs.html", context)


def blog_details(request, id):
    blogs = data["blogs"]
    selectedBlog = None
    for blog in blogs:
        if blog["id"] == id:
            selectedBlog = blog

    return render(request, "blog/blog-details.html", {"blog": selectedBlog})
