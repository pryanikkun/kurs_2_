from flask import Blueprint, render_template, redirect
from app.posts.dao.posts_dao import PostsDAO
from app.bookmarks.dao.bookmarks_dao import BookmarksDAO

bookmarks_blueprint = Blueprint('bookmarks_blueprint', __name__, url_prefix='/bookmarks')
posts = PostsDAO('./data/posts.json', './data/comments.json')
bookmarks = BookmarksDAO('./data/bookmarks.json')


@bookmarks_blueprint.route('/')
def page_bookmarks():
    """ Выводит все закладки """
    book = bookmarks.load_bookmarks()
    return render_template('bookmarks.html', bookmarks=book, len_book=len(book))


@bookmarks_blueprint.route('/add/<int:post_id>')
def page_bookmarks_add(post_id):
    """ Добавление поста в bookmarks.json и переадресация на главную страницу """
    post = posts.get_post_by_pk(post_id)
    bookmarks.bookmarks_add(post)
    return redirect('/', code=302)


@bookmarks_blueprint.route('/remove/<int:post_id>')
def page_bookmarks_remove(post_id):
    """ Удаление поста из bookmarks.json и переадресация на главную страницу """
    post = posts.get_post_by_pk(post_id)
    bookmarks.bookmarks_remove(post)
    return redirect('/', code=302)
