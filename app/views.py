from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from datetime import datetime, timezone
import json

from . import db
from .models import Article

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
    return render_template("home.html")
