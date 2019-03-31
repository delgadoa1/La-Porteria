from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()                         # Objects is referencing the SQL database
    }
    return render(request, 'blog/home.html', context)       # What the user sees on the site/blog page


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})      # What the user sees on the site/about page
