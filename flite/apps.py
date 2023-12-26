from django.apps import AppConfig


class FliteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'flite'


from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return 'Добро пожаловать на главную страницу!'


@app.route('/register', methods=['POST'])
def register():
    # Получение данных из формы
    username = request.form['username']
    password = request.form['password']

    # Можно добавить код для обработки и сохранения данных (например, в базу данных)

    # Перенаправление на главную страницу
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
