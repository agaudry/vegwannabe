from marshmallow import Schema, fields
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db = SQLAlchemy()


class Food(db.Model):
    __tablename__ = "food"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    quantity = db.Column(db.Integer)
    date = db.Column(db.DateTime)
    reason = db.Column(db.String(255))
    user_id = db.Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="foods")


class FoodSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    quantity = fields.Int()
    date = fields.DateTime()
    reason = fields.Str()


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(512), nullable=False)
    foods = relationship("Food", back_populates="user")

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    email = fields.Str()
    password = fields.Str()
