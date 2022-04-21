from django.shortcuts import render
from .models import *

# Create your views here.


def show_posts(request):
    posts = Post.objects.all()
    print(posts.get().title)
    return render(request, "post_list.html", {"posts": posts})
