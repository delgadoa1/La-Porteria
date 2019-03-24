from django.shortcuts import render

"""
All views are what the user will see on the web page
"""


posts = [
    {
        "author": "Andres Delgado",
        "title": "Property 1",
        "content": "Add description and pics of property 1",
        "date_posted": "Mar 2019"
    },
    {
        "author": "Alex Delgado",
        "title": "Property 2",
        "content": "Add description and pics of property 2",
        "date_posted": "Mar 2019"
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)       # What the user sees on the site/blog page


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})      # What the user sees on the site/about page
