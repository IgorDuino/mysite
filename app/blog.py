from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required

from . import db
from .models import Article

blog = Blueprint('blog', __name__)


@blog.route('/', methods=['GET', 'POST'])
def blog_home():
    articles = db.session.query(Article).all()
    return render_template("blog.html", articles=articles)


@blog.route('/create', methods=['GET', 'POST'])
@login_required
def blog_create_article():
    if request.method == 'POST':
        article_title = request.form.get('article_title')
        article_url = request.form.get('article_url')

        return redirect(url_for("blog.blog_home"))

    return render_template("create_article.html")


@blog.route('/<article_url>', methods=['GET', 'POST'])
def blog_article(article_url):
    article = db.session.query(Article).filter(Article.url == article_url).first()

    if article:
        article: Article
        return render_template("article.html", article=article)
    else:
        return render_template("404.html"), 404
