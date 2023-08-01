from django.test import TestCase
from main_lib.models import Book, Author
import unittest
from django.test import Client
from django.urls import reverse

class BookTestCase(TestCase):
    def setUp(self):
        self.author = Author.objects.create(author_name='Test Author')
        self.book = Book.objects.create(book_title='Test Book')
        self.book.authors.set([self.author])

    def test_book_list_view(self):
        url = reverse('main_lib:book_view_all')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.book.book_title)
        print("THIRD CHECKPOINT", response, self.book.book_title)

    def test_book_create_view(self):
        url = reverse('main_lib:book_add')
        data = {'book_title': 'Test Book', 'authors': self.author.pk}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Book.objects.filter(book_title='Test Book').exists())

    def test_book_detail_view(self):
        url = reverse('main_lib:book_detail', args=[self.book.pk])
        response = self.client.get(url)
        print("SECCOND CHECKPOINT", response.content)
        self.assertEqual(response.status_code, 200)
        print("FIRST CHECKPOINT", self.book.book_title)
        self.assertContains(response, self.book.book_title)

    def test_book_update_view(self):
        url = reverse('main_lib:book_update', args=[self.book.pk])
        data = {'book_title': 'Updated Book', 'authors': self.author.pk}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Book.objects.filter(book_title='Updated Book').exists())

    def test_book_delete_view(self):
        url = reverse('main_lib:book_delete', args=[self.book.pk])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Book.objects.filter(book_title='Test Book').exists())