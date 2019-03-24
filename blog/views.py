from django.shortcuts import render
from django.http import HttpResponse

"""
All views are what the user will see on the web page
"""


posts = [
    {
        "author": "Andres",
        "title": "Blog Post 1",
        "content": "First Post Content",
        "date_posted": "Mar 2019"
    },
    {
        "author": "John",
        "title": "Blog Post 2",
        "content": "Second Post Content",
        "date_posted": "Mar 2019"
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)       # What the user sees on the site/blog page


def about(request):
    return render(request, 'blog/about.html', {'title':'About'})      # What the user sees on the site/about page
