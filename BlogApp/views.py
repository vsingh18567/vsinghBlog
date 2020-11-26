from django.urls.base import reverse_lazy
from .models import Post
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import *

# Create your views here.
class Home(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-date']

class Article(DetailView):
    model = Post
    template_name = 'article.html'

class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'
    # fields = ('author', 'title', 'body')

class EditPost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'edit_post.html'

class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('blog-home')