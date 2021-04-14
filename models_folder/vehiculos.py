from app import db
from sqlalchemy import ForeignKey


class Vehiculo(db.Model):
    id_vehiculo = db.Column(db.Integer, primary_key=True, attribute="id")
    id_marca = db.Column(db.String,
                         ForeignKey('marca.id'),
                         nullable=False)
    color = db.Column(db.String, nullable=False)
    patente = db.Column(db.String, nullable=False)
    id_relacion = db.Column(db.Integer,
                            ForeignKey('personaVehiculo.id'),
                            attribute="id")

db.create_all()