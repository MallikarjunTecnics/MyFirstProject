from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from Books.models import Author

class AuthorTests(APITestCase):
    def setUp(self):
        self.author = Author.objects.create(author_id=1, name='Test Author', email='test.author@example.com')
        
    def test_get_author_list(self):
        url = reverse('author-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)
        self.assertIn('author_id', response.data[0])
        self.assertIn('name', response.data[0])
        self.assertIn('email', response.data[0])

    def test_create_author(self):
        url = reverse('author-list')
        data = {'author_id': 2, 'name': 'New Author', 'email': 'new.author@example.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.count(), 2)

class AuthorTests1(APITestCase):
    def setUp(self):
        Author.objects.create(author_id=1, name='Author 1', email='author1@example.com')
        Author.objects.create(author_id=2, name='Author 2', email='author2@example.com')
        Author.objects.create(author_id=3, name='Author 3', email='author3@example.com')
        Author.objects.create(author_id=4, name='Author 4', email='author4@example.com')
        # Author.objects.create(author_id=5, name='Author 5', email='author5@example.com')

    def test_author_count(self):
        authors_count = Author.objects.count()
        self.assertEqual(authors_count, 4)

    def test_author_object_count(self):
        authors_count = Author.objects.count()
        self.assertLessEqual(authors_count, 4, f"Expected less than or equal to 4 authors but found {authors_count}")

