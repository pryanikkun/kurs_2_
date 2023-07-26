import json


class PostsDAO:

    def __init__(self, path_posts, path_comments):
        self.path_posts = path_posts
        self.path_comments = path_comments

    def load_posts(self):
        """ Загрузка постов из posts.json и замена тэгов """
        with open(self.path_posts, 'r', encoding='utf-8') as file:
            data = json.load(file)

        for post in data:
            words = post['content'].split(' ')
            tags = []
            for word in words:
                if '#' in word:
                    tags.append(word)
            content = ' '.join(words)
            if tags != []:
                for tag in tags:
                    content = content.replace(tag, f'<a href="/tag/{tag[1:]}" class="item__tag">{tag}</a> ', 1)
            post['content'] = content

        return data

    def load_comments(self):
        """ Загрузка комментариев из comments.json """
        with open(self.path_comments, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    def get_all_posts(self):
        """ Получение всех постов """
        posts = self.load_posts()
        return posts

    def get_posts_by_user(self, user_name):
        """ Получение постов по имени пользователя """
        posts = self.load_posts()
        users = set([x['poster_name'] for x in posts])
        user_posts = []

        if user_name not in users:
            raise ValueError('Такого пользователя не существует')

        for post in posts:
            if user_name == post['poster_name']:
                user_posts.append(post)

        return user_posts

    def search_for_posts(self, query):
        """ Поиск постов по запросу """
        posts = self.load_posts()
        query_posts = []
        for post in posts:
            if query.lower() in post['content'].lower():
                query_posts.append(post)
        return query_posts

    def get_post_by_pk(self, pk):
        """ Получение постов по номеру """
        posts = self.load_posts()
        for post in posts:
            if pk == post['pk']:
                return post

    def get_comments_by_post_id(self, post_id):
        """ Получение комментов по id """
        comments = self.load_comments()
        posts = self.load_posts()
        post_id_comments = []

        if post_id > len(posts):
            raise ValueError('Поста с таким id не существует')

        for comment in comments:
            if post_id == comment['post_id']:
                post_id_comments.append(comment)

        return post_id_comments
