import os
from decouple import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = config('FLASK_SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URI')

    db.init_app(app)

    migrate = Migrate(app, db)

    from .views import views
    from .auth import auth
    from .blog import blog

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(blog, url_prefix='/blog')

    from .models import User, Article

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
