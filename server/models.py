from app import db
from marshmallow import Schema, fields


class Food(db.Model):
    __tablename__ = "food"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    quantity = db.Column(db.Integer)
    date = db.Column(db.DateTime)
    reason = db.Column(db.String(255))


class FoodSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    quantity = fields.Int()
    date = fields.DateTime()
    reason = fields.Str()
