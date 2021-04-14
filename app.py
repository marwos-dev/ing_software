from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root:{os.environ["PWBD"]}@{os.environ["HOSTBD"]}/{os.environ["NAMEBD"]}' # noqa
db = SQLAlchemy(app)


from models import Marcas, Persona, PersonaVehiculo, Vehiculo


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html', data=dict())


marcas = db.session.query(Marcas).all()

print("hola")
#for marca in Marcas:
#    print (marca.idMarca)
#    print (marca.nombreMarca)


##agregar una nueva marca
nueva_marca=(Marcas(nombre='Audi'))
db.session.add(nueva_marca)
db.session.commit()


##Buscar por parametro
Marca_por_nombre=db.session.query(Marcas).filter(Marcas.nombre=='Ford').first()
print(Marca_por_nombre.id, Marca_por_nombre.nombre)

#Borrar registro

#Marca_a_borrar=db.session.query(Marca).filter(Marca.nombreMarca=='Audi').first()
#db.session.delete(Marca_a_borrar)
#db.session.commit()

#Editar un Registro
Editar_registro=db.session.query(Marca).filter(Marca.idMarca=='2').first()
Editar_registro.nombreMarca='Zanella'
db.session.commit()


Vehiculos=db.session.query(Vehiculo).all()

#Joins con Alchemy
VehiculoMarca=db.session.query(Marca,Vehiculo).join(Vehiculo,Vehiculo.idMarca==Marca.idMarca).filter(Marca.nombreMarca=='Zanella').all()
for vehiculo in VehiculoMarca:
    print(vehiculo.Vehiculo.nombreVehiculo)
    print(vehiculo.Marca.nombreMarca)



#Obtener el listado de personas

#Obtener modelos de los vehiculos < 2019

#Obtener todos los vehiculos de la marca Fiat

#Obtener los modelos de los vehiculo de la marca Fiat

#Obtener todas las personas que tengan un Ford


#Borrar Chevrolet
