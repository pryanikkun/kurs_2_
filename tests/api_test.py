import pytest
from tests.conftest import test_client

keys_should_be = {'poster_name', 'poster_avatar', 'likes_count',
                  'pic', 'pk', 'content', 'views_count'}


class TestApiViews:

    def test_page_api_posts(self, test_client):
        response = test_client.get('/api/posts/', follow_redirects=True)
        assert response.status_code == 200, 'Статус-код не 200'
        assert type(response.json) == list, 'Возвращается не список'
        assert set(response.json[0].keys()) == keys_should_be, 'Ключи не те'

    def test_page_api_post(self, test_client):
        response = test_client.get('/api/posts/1', follow_redirects=True)
        assert response.status_code == 200, 'Статус-код не 200'
        assert type(response.json) == dict, 'Возвращается не список'
        assert set(response.json.keys()) == keys_should_be, 'Ключи не те'
