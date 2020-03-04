from app import db
from marshmallow import Schema, fields

class DoDontItems(db.Model):
    __tablename__ = 'dodontitems'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    category = db.Column(db.String(64))

class Dos(db.Model):
    __tablename__ = 'dos'
    id = db.Column(db.Integer, primary_key=True)
    parent_name = db.Column(db.String(64))
    begin_at = db.Column(db.DateTime)
    end_at = db.Column(db.DateTime)

class Donts(db.Model):
    __tablename__ = 'donts'
    id = db.Column(db.Integer, primary_key=True)
    parent_name = db.Column(db.String(64))


class DoDontItemsSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    category = fields.Str()

class DosSchema(Schema):
    id = fields.Int()
    parent_name = fields.Str()
    begin_at = fields.DateTime()
    end_at = fields.DateTime()

class DontsSchema(Schema):
    id = fields.Int()
    parent_name = fields.Str()