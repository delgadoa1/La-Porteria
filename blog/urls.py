from django.urls import path
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    UserPostListView)
from . import views

"""
These paths are what redirect the user to the correct view on the site. '' means the home page which is currently
redirecting to the "Blog Home." Make sure to create a view.x where x is the subject of the page the person will view.
views.home for home page, views.about for about page, etc.
"""

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),  # localhost:8000 Home Page
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about')      # localhost:8000/about

]
