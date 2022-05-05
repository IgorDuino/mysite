from flask import Blueprint, render_template, make_response
from flask_login import current_user


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html")

@views.route("/sitemap.xml")
def sitemap_xml():
    response= make_response(render_template("sitemap.xml"))
    response.headers['Content-Type'] = 'application/xml'
    return response

@views.route("/robots.txt")
def robots_txt():
    return render_template("robots.txt")


# @views.app_errorhandler(Exception)
# def blog_error_handler(error):
#     return render_template("error.html", error=error)
