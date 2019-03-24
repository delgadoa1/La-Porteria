from django.urls import path
from . import views         # "." means current directory

"""
These paths are what redirect the user to the correct view on the site. '' means the home page which is currently
redirecting to the "Blog Home." Make sure to create a view.x where x is the subject of the page the person will view.
views.home for home page, views.about for about page, etc.
"""

urlpatterns = [
    path('', views.home, name='blog-home'),             # localhost:8000 Home Page
    path('about/', views.about, name='blog-about')      # localhost:8000/about

]
