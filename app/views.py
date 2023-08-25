# from django.shortcuts import render,redirect
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Blog,Comment
from .forms import BlogForm,CommentForm

# Create your views here.

# ----------------- LISTVIEW --------------------

class Home(ListView):
    model = Blog
    template_name = "index/home.html"
    ordering = ['-id']

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'index/readmore.html'


class AddBlog(CreateView):
    model = Blog
    form_class = BlogForm
    template_name = "index/addblog.html"
    # fields = "__all__"
    

class EditBlog(UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = "index/update.html"
    # fields = "__all__"
    
class DeleteBlog(DeleteView):
    model = Blog
    template_name = "index/delete.html"
    success_url = reverse_lazy("home")
    
class AddComment(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "index/commentsection.html"
    success_url = reverse_lazy("home")
    
    def form_valid(self,form):
        form.instance.blog.id = self.kwargs[id]
        return super().form_valid(form)