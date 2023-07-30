from django.contrib import admin
from django.urls import path, include
from . import views


app_name = 'main_lib'

urlpatterns = [
    #author part
    path('view_authors', views.AuthorListView.as_view(), name='view_authors'),
    path('add_author', views.AuthorCreateView.as_view(), name='add_author'),
    path('edit_author/<int:pk>', views.AuthorUpdateView.as_view(), name='edit_author'),
    path('delete_author/<int:pk>', views.AuthorDeleteView.as_view(), name='delete_author'),
    #book part
    path('view_book', views.BookListView.as_view(), name='book_view_all'),
    path('book_add', views.BookCreateView.as_view(), name='book_add'),
    path('book_detail/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),
    path('book_update/<int:pk>', views.BookUpdateView.as_view(), name='book_update'),
    path('book_delete/<int:pk>', views.BookDeleteView.as_view(), name='book_delete')
]