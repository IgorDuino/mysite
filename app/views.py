from flask import Blueprint, render_template
from flask_login import current_user

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    # if request.method == 'POST':
    #     title = request.form.get('title')
    #     desc = request.form.get('desc')
    #     new_todo = Todo(todo=title, desc=desc, user_id=current_user.id)
    #     db.session.add(new_todo)
    #     db.session.commit()
    #     flash('Todo created successfully!', category='success')
    print(current_user)
    return render_template("home.html")


@views.app_errorhandler(Exception)
def blog_error_handler(error):
    return render_template("error.html", error=error)
