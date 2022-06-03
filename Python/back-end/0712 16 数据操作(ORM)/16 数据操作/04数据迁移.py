from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)


class Config:
    # 数据库链接配置参数
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///school.db'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1/school'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_ECHO = True
    SECRET_KEY = 'secret key'


app.config.from_object(Config)

# 创建数据库链接对象
db = SQLAlchemy()
migrate = Migrate()

db.init_app(app)
migrate.init_app(app, db)


class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(length=20))

    gender = db.Column(db.String(length=20))
    # birth = db.Column(db.String(length=20))
    # phone = db.Column(db.String(length=20))

    def __repr__(self):
        return '<Students %s>' % self.username
