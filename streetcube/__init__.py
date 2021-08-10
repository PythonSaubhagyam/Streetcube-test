from functools import wraps

# Import flask and template operators
from flask import Flask, render_template,session, blueprints,jsonify
# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager,login_required


from flask_wtf.csrf import CSRFProtect,CSRFError
import logging

from logging.handlers import RotatingFileHandler


# Define the WSGI application object
app = Flask(__name__, static_url_path = '/static')

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'main.login'
login_manager.session_protection="None"
login_manager.login_message = "Please Log In"
login_manager.login_message_category = "danger"


from streetcube.home.controller import main
from streetcube.admin.controller import admin
from streetcube.front.frontController import front

# Register blueprint(s)
app.register_blueprint(main)
app.register_blueprint(admin)
app.register_blueprint(front)

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()





