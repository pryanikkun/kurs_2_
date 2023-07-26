from flask import Blueprint, render_template, request
from app.posts.dao.posts_dao import PostsDAO
from app.bookmarks.dao.bookmarks_dao import BookmarksDAO

posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder='templates')
posts = PostsDAO('./data/posts.json', './data/comments.json')
bookmarks = BookmarksDAO('./data/bookmarks.json')


@posts_blueprint.route('/')
def page_index():
    """ Возвращает главную страницу """
    return render_template('index.html', posts=posts.load_posts(), len_book=len(bookmarks.load_bookmarks()))


@posts_blueprint.route('/posts/<int:post_id>')
def page_comments(post_id):
    """ Возвращает страницу поста """
    post = posts.get_post_by_pk(post_id)
    comments = posts.get_comments_by_post_id(post_id)
    return render_template('post.html', post=post, comments=comments)


@posts_blueprint.route('/search/')
def page_search():
    """ Возвращает страницу с найденными по слову постами """
    s = request.values.get('s')
    found_posts = posts.search_for_posts(s)
    return render_template('search.html', len_posts=len(found_posts), posts=found_posts)


@posts_blueprint.route('/users/<username>')
def page_users(username):
    """ Возвращает страницу пользователя с его постами """
    post = posts.get_posts_by_user(username)
    return render_template('user-feed.html', username=username, posts=post)


@posts_blueprint.route('/tag/<tagname>')
def page_tags(tagname):
    """ Возвращает страницу с постами по тэгу"""
    tag = '#' + tagname
    tag_posts = posts.search_for_posts(tag)
    return render_template('tag.html', tag=tag, tagname=tagname, posts=tag_posts)
