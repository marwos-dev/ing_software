from app import db


class Persona(db.Model):
    id_persona = db.Column(db.Integer, primary_key=True, attribute="id")
    nombre = db.Column(db.Integer, nullable=False)
    id_relacion = db.Column(db.Integer, primary_key=True, attribute="id")

db.create_all()
