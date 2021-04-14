from app import db
from sqlalchemy import ForeignKey


class Marcas(db.Model):
    id_marca = db.Column(db.Integer, primary_key=True, attribute="id")
    nombre = db.Column(db.String, nullable=False)


class PersonaVehiculo(db.Model):
    id_relacion = db.Column(db.Integer, primary_key=True, attribute="id")
    id_persona = db.Column(db.Integer,
                           ForeignKey('persona.id'),
                           nullable=False)
    id_vehiculo = db.Column(db.Integer,
                            ForeignKey('vehiculo.id'),
                            nullable=False)


class Persona(db.Model):
    id_persona = db.Column(db.Integer, primary_key=True, attribute="id")
    nombre = db.Column(db.Integer, nullable=False)
    id_relacion = db.Column(db.Integer, primary_key=True, attribute="id")


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