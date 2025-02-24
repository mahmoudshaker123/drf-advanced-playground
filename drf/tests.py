import pytest
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from .models import Article
from django.contrib.auth.models import User


@pytest.mark.django_db
class ArticleAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.article = Article.objects.create(title='Test Article', content='Test Content', owner=self.user)

    def test_unauthenticated_user_cannot_add_article(self):
        url = reverse('article-list')
        data = {'title': 'New Article', 'content': 'New Content'}
        response = self.client.post(url, data, format='json')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_authenticated_user_can_create_article(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('article-list')
        data = {'title': 'New Article', 'content': 'New Content'}
        response = self.client.post(url, data, format='json')
        assert response.status_code == status.HTTP_201_CREATED

    def test_user_can_update_own_article(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('article-detail', args=[self.article.id])
        data = {'title': 'Updated Title', 'content': 'Updated Content'}
        response = self.client.put(url, data, format='json')
        assert response.status_code == status.HTTP_200_OK
        self.article.refresh_from_db()
        assert self.article.title == 'Updated Title'

    def test_user_can_delete_own_article(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('article-detail', args=[self.article.id])
        response = self.client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Article.objects.filter(id=self.article.id).count() == 0

    def test_pagination_returns_five_articles_per_page(self):
        self.client.login(username='testuser', password='testpassword')
        for i in range(10):
            Article.objects.create(title=f'Article {i}', content='Content', owner=self.user)
        url = reverse('article-list')
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['results']) == 5

    def test_search_articles_by_title_and_content(self):
        self.client.login(username='testuser', password='testpassword')
        Article.objects.create(title='Searchable Title', content='Searchable Content', owner=self.user)
        url = reverse('article-list')
        response = self.client.get(url, {'search': 'Searchable'})
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['results']) > 0

    def test_ordering_articles_by_created_at(self):
        self.client.login(username='testuser', password='testpassword')
        Article.objects.create(title='Older Article', content='Older Content', owner=self.user)
        Article.objects.create(title='Newer Article', content='Newer Content', owner=self.user)
        url = reverse('article-list')
        response = self.client.get(url, {'ordering': 'created_at'})
        assert response.status_code == status.HTTP_200_OK
        articles = response.data['results']
        assert articles[0]['title'] == 'Older Article'
        assert articles[1]['title'] == 'Newer Article'