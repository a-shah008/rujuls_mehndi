from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = '3e7bf39c2f9a3470ee4d10cc96685b36'
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
    
    db.init_app(app)

    return app

app = create_app()
app.app_context().push()

db.drop_all()
db.create_all()

from app import routes