from app import db
from sqlalchemy import ForeignKey


class PersonaVehiculo(db.Model):
    id_relacion = db.Column(db.Integer, primary_key=True, attribute="id")
    id_persona = db.Column(db.Integer,
                           ForeignKey('persona.id'),
                           nullable=False)
    id_vehiculo = db.Column(db.Integer,
                            ForeignKey('vehiculo.id'),
                            nullable=False)

db.create_all()
