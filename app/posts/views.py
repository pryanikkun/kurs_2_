from flask import Blueprint, render_template, request
from app.posts.dao.posts_dao import PostsDAO

posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder='templates')
posts = PostsDAO('./data/posts.json', './data/comments.json')


@posts_blueprint.route('/')
def page_index():
    return render_template('index.html', posts=posts.load_posts())


@posts_blueprint.route('/posts/<int:post_id>')
def page_comments(post_id):
    post = posts.get_post_by_pk(post_id)
    comments = posts.get_comments_by_post_id(post_id)
    return render_template('post.html', post=post, comments=comments)


@posts_blueprint.route('/search/')
def page_search():
    s = request.values.get('s')
    post = posts.search_for_posts(s)
    return render_template('search.html', len_posts=len(post), posts=post)


@posts_blueprint.route('/users/<username>')
def page_users(username):
    post = posts.get_posts_by_user(username)
    return render_template('user-feed.html', username=username, posts=post)
