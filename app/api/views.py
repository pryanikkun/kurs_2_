import logging
from flask import Blueprint, jsonify
from app.posts.dao.posts_dao import PostsDAO

posts = PostsDAO('./data/posts.json', './data/comments.json')
api_blueprint = Blueprint('api_blueprint', __name__, url_prefix='/api')
logging.basicConfig(filename='api.log', level=logging.INFO, encoding='utf-8',
                    format='%(asctime)s %(levelname)s %(message)s')


@api_blueprint.route('/posts/')
def page_api_posts():
    """ Возвращает список всех постов в .json списка"""
    all_posts = posts.get_all_posts()
    logging.info('Запрос /api/posts/')
    return jsonify(all_posts)


@api_blueprint.route('/posts/<int:post_id>')
def page_api_post(post_id):
    logging.info(f'Запрос /api/posts/{post_id}')
    post = posts.get_post_by_pk(post_id)
    return jsonify(post)
