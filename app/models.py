from flask_login import UserMixin
from sqlalchemy.sql import func

from . import db


def generate_article_url(article_id: int, article_title: str) -> str:
    char_to_replace = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh', 'з': 'z',
                       'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
                       'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'cz', 'ш': 'sh', 'щ': 'scz',
                       'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'u', 'я': 'ja', 'А': 'A', 'Б': 'B', 'В': 'V',
                       'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E', 'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K',
                       'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
                       'Ф': 'F', 'Х': 'H', 'Ц': 'C', 'Ч': 'CZ', 'Ш': 'SH', 'Щ': 'SCH', 'Ъ': '', 'Ы': 'y', 'Ь': '',
                       'Э': 'E', 'Ю': 'U', 'Я': 'YA', ',': ' ', '?': ' ', '~': ' ', '!': ' ', '@': ' ', '#': ' ',
                       '$': ' ', '%': ' ', '^': ' ', '&': ' ', '*': '', '(': ' ', ')': ' ', '-': ' ', '=': ' ',
                       '+': ' ', ':': ' ', ';': ' ', '<': ' ', '>': ' ', '\'': ' ', '"': ' ', '\\': ' ', '/': ' ',
                       '№': ' ', '[': ' ', ']': ' ', '{': ' ', '}': ' ', 'ґ': '', 'ї': '', 'є': '', 'Ґ': 'g', 'Ї': 'i',
                       'Є': 'e', '—': ' ', '.': ' '}

    for key, value in char_to_replace.items():
        title = article_title.replace(key, value)

    article_title = "_".join(article_title.lower().split())

    article_title += f'_{article_id}'

    return article_title


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    is_admin = db.Column(db.Boolean, default=False)
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    articles = db.relationship('Article')


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False)
    hidden = db.Column(db.Boolean, default=False)
    url = db.Column(db.String(500))
    content = db.Column(db.Text)
    views = db.Column(db.Integer, default=0)
    rating = db.Column(db.Integer, default=10)
    date = db.Column(db.DateTime(timezone=True), default=func.now(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
