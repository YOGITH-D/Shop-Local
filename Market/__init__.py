from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///market.db'
app.config['SECRET_KEY']='95b89d6d06b99e49dcd857c2'
bycrypt=Bcrypt(app)
db=SQLAlchemy(app)
login_manager=LoginManager(app)
login_manager.login_view="login_page"
from Market import routes