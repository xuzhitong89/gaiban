#coding=utf8
import hashlib
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost:3306/test1'
db = SQLAlchemy(app)  #这个就是你以后操作数据库的对象实例了
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(320), unique=True)
    password = db.Column(db.String(32), nullable=False)
  
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
  
    def __repr__(self):
        return "<User '{:s}'>".format(self.username)
if __name__ == '__main__':
    db.create_all()
    '''u = User(username='peter', email='test@example.com', password='123456')
    db.session.add(u)
    db.session.commit()
    '''
