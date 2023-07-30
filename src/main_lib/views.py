from django.shortcuts import render
from django.views import generic
from . import models
from django.urls import reverse_lazy
# Create your views here.

#Author part
class AuthorListView(generic.ListView):
    model = models.Author
    template_name = "author/view_authors.html"


class AuthorCreateView(generic.CreateView):
    model = models.Author
    success_url = reverse_lazy('main_lib:view_authors')
    fields = ['author_name', 'author_description']
    template_name = 'author/add_author.html'
    
    
class AuthorUpdateView(generic.UpdateView):
    model = models.Author
    success_url = reverse_lazy('main_lib:view_authors')
    fields = ['author_name', 'author_description']
    template_name = 'author/edit_author.html'


class AuthorDeleteView(generic.DeleteView):
    model = models.Author
    success_url = reverse_lazy('main_lib:view_authors')
    template_name = 'author/delete_author.html'
    
    
 #Book part
    
class BookListView(generic.ListView):
    model = models.Book
    template_name = "book/book_view_all.html"


class BookCreateView(generic.CreateView):
    model = models.Book
    template_name = 'book/book_add.html'
    success_url = reverse_lazy('main_lib:book_view_all')
    fields = ['book_title', 'authors',]


class BookDetailView(generic.DetailView):
    model = models.Book
    template_name = 'book/book_detail.html'


class BookUpdateView(generic.UpdateView):
    model = models.Book
    template_name = 'book/book_update.html'
    fields = ['book_title', 'authors',]
    success_url = reverse_lazy('main_lib:book_view_all')


class BookDeleteView(generic.DeleteView):
    model = models.Book
    template_name = 'book/book_delete.html'
    success_url = reverse_lazy('main_lib:book_view_all')