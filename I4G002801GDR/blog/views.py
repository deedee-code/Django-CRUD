from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView
from .models import Post

class PostListView(ListView):
    model = Post

from django.views.generic import CreateView
from .models import Post

class PostCreateView(CreateView):
    model = Post
    fields = '__all__'
    success_url  = reverse_lazy('blog:all')

from django.views.generic import DetailView
from .models import Post

class PostDetailView(DetailView):
    model = Post

from django.views.generic import UpdateView
from .models import Post

class PostUpdateView(UpdateView):
    model = Post
    fields = '__all__'
    success_url  = reverse_lazy('blog:all')

from django.views.generic import DeleteView
from .models import Post

class PostDeleteView(DeleteView):
    model = Post
    fields = '__all__'
    success_url  = reverse_lazy('blog:all')

