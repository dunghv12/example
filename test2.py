from Restapi.extension import db
from sqlalchemy import Column,Integer,String
from sqlalchemy import Column,Integer,String

class Pipi(db.Model):
    __tablename__ = 'pipi'
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