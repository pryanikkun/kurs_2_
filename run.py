from flask import Flask
from app.posts.views import posts_blueprint
from app.api.views import api_blueprint

app = Flask(__name__)
app.config.from_pyfile('config.py')

app.register_blueprint(posts_blueprint)
app.register_blueprint(api_blueprint)

if __name__ == '__main__':
    app.run()


@app.errorhandler(404)
def page_error_404(e):
    return '<h2>Такой страницы не существует (во всяком случае пока)</h2> <br> <a href="/" class="link">Назад</a>', 404


@app.errorhandler(500)
def page_error_500(e):
    return '<h2> Ошибка сервера </h2><br><a href="/" class="link">Назад</a>', 500
