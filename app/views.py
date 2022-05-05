from flask import Blueprint, render_template
from flask_login import current_user


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html")


@views.app_errorhandler(Exception)
def blog_error_handler(error):
    return render_template("error.html", error=error)
