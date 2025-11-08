from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    path("", PostListView.as_view(), name="PostListView"),
    path("blog/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("blog/create/", PostCreateView.as_view(), name="Post_create"),
    path("blog/<int:pk>/update/", PostUpdateView.as_view(), name="post_update"),
    path("blog/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
]