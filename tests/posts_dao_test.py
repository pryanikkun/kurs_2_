import pytest
from app.posts.dao.posts_dao import PostsDAO

keys_should_be = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}


@pytest.fixture()
def posts_dao():
    posts_dao_instance = PostsDAO('./data/posts.json', './data/comments.json')
    return posts_dao_instance


class TestPostsDAO:

    def test_get_all_posts(self, posts_dao):
        posts = posts_dao.get_all_posts()
        assert type(posts) == list, 'Структура posts.json не список'
        assert len(posts) > 0, 'Список постов пуст'
        assert set(posts[0].keys()) == keys_should_be, 'Набор ключей не тот'

    def test_get_posts_by_user(self,posts_dao):
        posts = posts_dao.get_posts_by_user('johnny')
        assert type(posts) == list, 'Структура не список'
        assert posts[0]['poster_name'] == 'johnny', 'Вернулись посты не того пользователя'
        assert len(posts) == 2, 'У джонни не 2 поста'
        assert set(posts[0].keys()) == keys_should_be, 'Набор ключей не тот'

    def test_get_posts_by_user_error(self, posts_dao):
        with pytest.raises(ValueError):
            posts_dao.get_posts_by_user('sonya')

    def test_search_for_posts(self, posts_dao):
        posts = posts_dao.search_for_posts('тАрелка')
        assert type(posts) == list, 'Структура не список'
        assert len(posts) == 1, 'Найдено неверное количество постов'
        assert set(posts[0].keys()) == keys_should_be, 'Набор ключей не тот'

    def test_get_post_by_pk(self, posts_dao):
        post = posts_dao.get_post_by_pk(2)
        assert type(post) == dict, 'Структура не словарь'
        assert post['pk'] == 2, 'Найден не тот пост'
        assert set(post.keys()) == keys_should_be, 'Набор ключей не тот'

    def test_get_comments_by_post_id_1(self, posts_dao):
        comments = posts_dao.get_comments_by_post_id(1)
        assert type(comments) == list, 'Структура не список'
        assert comments[0]['post_id'] == 1, 'Найден не тот комментарий'
        assert len(comments) == 4, 'Найдено неверное количество комментариев'

    def test_get_comments_by_post_id_8(self, posts_dao):
        comments = posts_dao.get_comments_by_post_id(8)
        assert type(comments) == list, 'Структура не список'
        assert len(comments) == 0, 'Найдено неверное количество комментариев'

    def test_get_comments_by_post_id_error(self, posts_dao):
        with pytest.raises(ValueError):
            posts_dao.get_comments_by_post_id(10)

