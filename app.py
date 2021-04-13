from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

Personas = {
    'usuario': [
        {
            "id": 1,
            "nombre": "Mariano",
            "password": "password123",
            "tipo": 1,
            "materias": [1, 2]
        },
        {
            "id": 2,
            "nombre": "Pablo",
            "password": "password_123",
            "tipo": 1,
            "materias": [1, 3]
        },
        {
            "id": 3,
            "nombre": "Carla",
            "password": "carla_4",
            "tipo": 1,
            "materias": [1, 3, 2]
        },
        {
            "id": 4,
            "nombre": "Maria",
            "password": "mariapaz123",
            "tipo": 1,
            "materias": [1, 2]
        },
        {
            "id": 5,
            "nombre": "Pedro",
            "password": "lemo_444",
            "tipo": 1,
            "materias": [1, 2]
        },
        {
            "id": 6,
            "nombre": "Pablo",
            "password": "Onur",
            "tipo": 1,
            "materias": [3, 2, 4]
        }
    ],
    'tipo': [
        {
            "id": 1,
            "tipo": "Alumno"
        }
    ],
    'Materias': [
        {
            "id": 1,
            "materia": "Programacion 1"
        },
        {
            "id": 2,
            "materia": "Lengua"
        },
        {
            "id": 3,
            "materia": "Programacion 2"
        },
        {
            "id": 4,
            "materia": "Base de Datos"
        },
    ]
}


@app.route('/login', methods=['GET', 'POST'])
def login():
    in_bd = False
    username = None
    materias = list()
    if request.method == 'POST':
        for persona in Personas['usuario']:
            print("gola")
            if persona['nombre'] == request.form['username'] and \
                    persona['password'] == request.form['password']:
                in_bd = True
                username = persona['nombre']
                for materia in persona['materias']:
                    for materias_data in Personas['Materias']:
                        if materia == materias_data['id']:
                            materias.append(materias_data)
        if in_bd:
            return render_template('home.html',
                                   usuario=username,
                                   materias=materias)
    if request.method == 'GET':
        return render_template('login.html')
    return render_template('login.html', error="No se encuentra el usuario")


@app.route('/materia/<int:id>')
def get_alumnos(id):
    alumnos = [alumno for alumno in Personas['usuario'] if id in alumno['materias']]
    nombre_clase = "none"
    for materia in Personas['Materias']:
        if materia['id'] == id:
            nombre_clase = materia['materia']
    return render_template('lista_alumnos.html', alumnos=alumnos,
                           nombre_clase=nombre_clase)


@app.route('/home')
def home(username: str, materias: list):
    if not username:
        return redirect(url_for('login'))
    return render_template('home.html', usuario=username, materias=materias)


if __name__ == '__main__':
    app.run()
