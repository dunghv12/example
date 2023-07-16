from Restapi.extension import db
from sqlalchemy import Column,Integer,String
from sqlalchemy import ARRAY
from flask_migrate import Migrate
from flask import Flask
from flask import Flask
from flask_migrate import Migrate

app=Flask(__name__)
class Books(db.Model):
    __tablename__ = 'books'
    id = db.Column(Integer,primary_key=True,autoincrement=True)
    name=db.Column(String(100),nullable=True)
    page_count=db.Column(Integer)
    author_id=db.Column(Integer, db.ForeignKey("author.id"))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    def __init__(self,name,page_count,author_id,category_id):
        self.name = name
        self.page_count = page_count


class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(Integer, primary_key=True,autoincrement=True)
    name=db.Column(String(100),nullable=True)
    birth=db.Column(db.Date)
    gender=db.Column(String(20))
    class_name = db.Column(String(20))
    # age=db.Column(Integer)
    def __init__(self,name,birth,gender,class_name,address):
        self.name = name
        self.birth = birth
        self.gender = gender
        self.class_name = class_name
        self.address=address

        
class Borrow(db.Model):
    __tablename__ = 'borrow'
    id = db.Column(Integer, primary_key=True,autoincrement=True)
    id_student=db.Column(Integer,db.ForeignKey("student.id"))
    id_books=db.Column(Integer,db.ForeignKey("books.id"))
    borrow_date=db.Column(db.Date)
    return_date = db.Column(db.Date)
    def __init__(self,id_student,id_books,borrow_date,return_date):
        self.id_student = id_student
        self.id_books = id_books
        self.borrow_date = borrow_date
        self.return_date = return_date


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name


class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    def __init__(self, name):
        self.name = name


class Role(db.Model):
    __tablename__ = 'role'
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    title=db.Column(db.String(100),nullable=False)
    def __init__(self,title):
        self.title = title


class EndPoint(db.Model):
    __tablename__ = 'endpoint'
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    endpoint=db.Column(db.String(100), nullable=False)
    method=db.Column(db.String(100),nullable=False)
    def __init__(self,endpoint,method):
        self.endpoint=endpoint
        self.method=method


class Accessbility(db.Model):
    __tablename__='accessbility'
    id=db.Column(db.Integer, primary_key=True)
    endpoint_id=db.Column(db.Integer,db.ForeignKey("endpoint.id"))
    role_id=db.Column(db.String(100))
    def __init__(self,endpoint_id,role_id):
        self.endpoint_id=endpoint_id
        self.role_id=role_id


class User(db.Model):
    __tablename__='user'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    password=db.Column(db.String(100),nullable=False)
    role_id=db.Column(db.Integer,db.ForeignKey("role.id"))
    def __init__(self,name,role_id,password):
        self.name=name
        self.role_id=role_id
        self.password=password


# class Test1(db.Model):
#     __tablename__='test'
#     id=db.Column(db.Integer,primary_key=True)
#     name=db.Column(db.String(100),nullable=False)
#     def __init__(self,name):
#         self.name=name


# class Test3(db.Model):
#     __tablename__='test3'
#     id=db.Column(db.Integer,primary_key=True)
#     name=db.Column(db.String(100),nullable=False)
#     def __init__(self,name):
#         self.name=name


# class Test4(db.Model):
#     __tablename__='test4'
#     id=db.Column(db.Integer,primary_key=True)
#     name=db.Column(db.String(100),nullable=False)
#     def __init__(self,name):
#         self.name=name





