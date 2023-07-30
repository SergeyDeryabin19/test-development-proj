from django.test import TestCase
from models import Book
import unittest
from django.test import Client
from django.urls import reverse

class BookTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_book_list(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_list.html')
        self.assertContains(response, 'List of all books')
        self.assertContains(response, 'Add book')

    def test_add_book(self):
        response = self.client.get(reverse('book_add'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_book.html')
        # Здесь можно добавить дополнительные проверки для формы добавления книги

    def test_edit_book(self):
        book = Book.objects.create(book_title='Test Book')
        url = reverse('book_update', args=[book.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_book.html')
        # Здесь можно добавить дополнительные проверки для формы редактирования книги

    def test_delete_book(self):
        book = Book.objects.create(book_title='Test Book')
        url = reverse('book_delete', args=[book.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_book.html')
        # Здесь можно добавить дополнительные проверки для формы удаления книги

if __name__ == '__main__':
    unittest.main()