from flask import Flask, request, render_template, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
import os


app = Flask(__name__)


db = SQLAlchemy(app)
bcrypt  = Bcrypt(app)
migrate=Migrate(app,db)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('abdelouaheddb')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
# import blueprints and register them
from pointage.main.routes import main
from pointage.admin.routes import admin
app.register_blueprint(main)
app.register_blueprint(admin)

