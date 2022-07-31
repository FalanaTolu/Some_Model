from django.shortcuts import render
from .models import Post


def home_view(request):
    greeting = "Hello, you are welcome"
    data = Post.objects.all()
    blog_post = {"greeting": greeting, "Posts": data}
    return render(request, "home.html", blog_post)