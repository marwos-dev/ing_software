from app import db


class Marcas(db.Model):
    id_marca = db.Column(db.Integer, primary_key=True, attribute="id")
    nombre = db.Column(db.String, nullable=False)

db.create_all()
