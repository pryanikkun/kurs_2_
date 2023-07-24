import pytest
from tests.conftest import test_client


class TestPostsViews:

    def test_page_index(self, test_client):
        response = test_client.get('/', follow_redirects=True)
        assert response.status_code == 200, 'Статус-код главной страницы не 200'

    def test_page_comments(self, test_client):
        response = test_client.get('/posts/5', follow_redirects=True)
        assert response.status_code == 200, 'Статус-код страницы поста не 200'

    def test_search_page(self, test_client):
        response = test_client.get('/search/?s=елки', follow_redirects=True)
        assert response.status_code == 200, 'Статус-код страницы поиска не 200'

    def test_user_page(self, test_client):
        response = test_client.get('/users/leo', follow_redirects=True)
        assert response.status_code == 200, 'Статус-код страницы пользователя не 200'
