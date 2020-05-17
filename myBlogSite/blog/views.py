from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import (TemplateView, CreateView, DetailView, 
                                ListView, DeleteView, UpdateView)

from blog.forms import PostForm, CommentForm
from blog.models import Post, Comment

from django.utils import timezone
from django.urls import reverse_lazy
# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'

# list the posts 
class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


# show details of a post
class PostDetailView(DetailView):
    model = Post

    
# create a post
class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm

    model = Post


# update a post
class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post


# delete a post
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')


# show drafts 
class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_draft_list.html'
    model = Post
    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('-created_date')
