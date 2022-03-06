import markdown
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user

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
    if not current_user.is_admin:
        return render_template("error.html", error=403), 403

    if request.method == 'POST':
        article_title = request.form.get('article_title')
        article_markdown_content = request.form.get('article_content')
        article_url = request.form.get('article_url')
        user_id = current_user.id

        article = Article()
        article.user_id = user_id
        article.title = article_title
        article.hidden = False
        article.url = article_url
        article.content_markdown = article_markdown_content
        article.content_html = markdown.markdown(article_markdown_content)

        db.session.add(article)
        db.session.commit()

        return redirect(url_for("blog.blog_home"))

    return render_template("create_article.html")


@blog.route('/<article_url>', methods=['GET', 'POST'])
def blog_article(article_url):
    article = db.session.query(Article).filter(Article.url == article_url).first()

    if article:
        article: Article
        return render_template("article.html", article=article)
    else:
        return render_template("error.html", error=404), 404


@blog.app_errorhandler(Exception)
def blog_error_handler(error):
    return render_template("error.html", error=error)
