from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from datetime import datetime, timezone
import json

from . import db
from .auth import login
from .models import Article

blog = Blueprint('blog', __name__)


def abcd():
    print(123)


@blog.route('/', methods=['GET', 'POST'])
def blog_home():
    articles = db.session.query(Article).all()
    return render_template("blog.html", articles=articles)


@blog.route('/create', methods=['GET', 'POST'])
@login_required
def create_article():
    return render_template("create_article.html")


@blog.route('/<article_url>', methods=['GET', 'POST'])
def blog_article(article_url):
    article = db.session.query(Article).filter(Article.url == article_url).first()
    if article:
        return render_template("article.html", article=article)
    else:
        return render_template("404.html"), 404