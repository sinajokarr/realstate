from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .models import Post
from .form import NewPostForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import UpdateView, DeleteView

class PostListView(generic.ListView):
    model = Post
    template_name ="blog/post_list.html"
    context_object_name = "post_list"

class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post_detail"

class PostCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = NewPostForm
    template_name = "blog/Post_create.html"
    success_url = reverse_lazy("PostListView")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,generic.UpdateView):
    form_class = NewPostForm
    template_name = "blog/post_create.html"
    model = Post

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,generic.DetailView):
    model = Post
    template_name = "blog/Post_delete.html"
    success_url = reverse_lazy("PostListView")

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user
