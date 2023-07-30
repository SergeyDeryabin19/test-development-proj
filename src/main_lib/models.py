from django.db import models

# Create your models here.

class Author(models.Model): 
    def __str__(self):
        return self.author_name
    
    def get_absolute_url(self):
        return '/success'
    
    author_name = models.CharField(verbose_name="Author name", max_length=255)
    author_description = models.TextField(verbose_name="Author description", null=True,blank=True)

class Book(models.Model):
    def __str__(self):
        return self.book_title
    
    def get_absolute_url(self):
        return '/success'
    
    book_title = models.CharField(verbose_name="Book title",max_length=100)
    authors = models.ManyToManyField(Author, verbose_name="Book author",)
   
    