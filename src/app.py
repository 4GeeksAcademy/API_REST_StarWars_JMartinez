"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for, json
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Planetas, Personajes, Usuario, Favoritos, Starships, Vehiculos
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

"""-----------------------------------------------------------------------------------------empoints - JMartinez-------------------------------------------------------------------- """

"""--------------------------------------------------------------------------------_<GIT ALL>_-------------------------------------------------------------------------------------"""

"""-----------------------------------------------_<Personajes>_------------------------------------------"""

@app.route('/personajes', methods=['GET'])
def get_personajes():

    #hacemos una consulta a la tabla planetas para que traiga todos los registros
    personajes_querys = Personajes.query.all()
    
     #mapeamos para convertir el array [<Planetas 1>] => un array de objetos
    results = list (map(lambda item: item.serialize(),personajes_querys))

    # control de error para array vacio
    if results == []:
        return jsonify({"msg": "No hay personajes"}), 404
    
    #regresamos una respuesta con los resultasos de la consulta 
    response_body = {

        "msg": "Hello, These are your personajes ",
        "results": results
    }

    return jsonify(response_body), 200

"""-----------------------------------------------_ </Personajes> _--------------------------------------"""

"""-----------------------------------------------_<Planetas>_-------------------------------------------"""

@app.route('/planetas', methods=['GET'])
def get_planets():

    #hacemos una consulta a la tabla planetas para que traiga todos los registros
    planets_querys = Planetas.query.all()

    #mapeamos para convertir el array [<Planetas 1>] => un array de objetos
    results = list (map(lambda item: item.serialize(),planets_querys))

    # control de error para array vacio
    if results == []:
        return jsonify({"msg": "No hay planetas"}), 404
    
    #regresamos una respuesta con los resultasos de la consulta 
    response_body = {

        "msg": "Hello, These are your planets ",
        "results": results
    }

    return jsonify(response_body), 200

"""-----------------------------------------------_ </Planets> _--------------------------------------"""

"""-----------------------------------------------_<Vehiculos>_---------------------------------------"""

@app.route('/vehiculos', methods=['GET'])
def get_vehiculos():

    #hacemos una consulta a la tabla planetas para que traiga todos los registros
    vehiculos_querys = Vehiculos.query.all()

    #mapeamos para convertir el array [<Planetas 1>] => un array de objetos
    results = list (map(lambda item: item.serialize(),vehiculos_querys))

    # control de error para array vacio
    if results == []:
        return jsonify({"msg": "No hay vehicles"}), 404
    
    #regresamos una respuesta con los resultasos de la consulta 
    response_body = {

        "msg": "Hello, These are your vehicles ",
        "results": results
    }

    return jsonify(response_body), 200

"""-----------------------------------------------_ </Vehiculos> _--------------------------------------"""

"""-----------------------------------------------_<Starships>_-----------------------------------------"""

@app.route('/starships', methods=['GET'])
def get_starships():

    #hacemos una consulta a la tabla planetas para que traiga todos los registros
    starships_querys = Starships.query.all()

    #mapeamos para convertir el array [<Planetas 1>] => un array de objetos
    results = list (map(lambda item: item.serialize(),starships_querys))

    # control de error para array vacio
    if results == []:
        return jsonify({"msg": "No hay starships"}), 404
    
    #regresamos una respuesta con los resultasos de la consulta 
    response_body = {

        "msg": "Hello, These are your starships ",
        "results": results
    }

    return jsonify(response_body), 200

"""-----------------------------------------------_ </Starships> _--------------------------------------"""

"""-----------------------------------------------_<Usuario>_-------------------------------------------"""

@app.route('/usuario', methods=['GET'])
def get_usuario():

    #hacemos una consulta a la tabla planetas para que traiga todos los registros
    usuario_querys = Usuario.query.all()

    #mapeamos para convertir el array [<Planetas 1>] => un array de objetos
    results = list (map(lambda item: item.serialize(),usuario_querys))

    # control de error para array vacio
    if results == []:
        return jsonify({"msg": "No hay users"}), 404
    
    #regresamos una respuesta con los resultasos de la consulta 
    response_body = {

        "msg": "Hello, These are your users ",
        "results": results
    }

    return jsonify(response_body), 200

"""-----------------------------------------------_ </Usuario> _--------------------------------------"""

"""-----------------------------------------------_<Favoritos>_-----------------------------------------"""

@app.route('/favoritos', methods=['GET'])
def get_favoritos():

    #hacemos una consulta a la tabla planetas para que traiga todos los registros
    favoritos_querys = Favoritos.query.all()

    #mapeamos para convertir el array [<Planetas 1>] => un array de objetos
    results = list (map(lambda item: item.serialize(),favoritos_querys))

    # control de error para array vacio
    if results == []:
        return jsonify({"msg": "No hay favorites"}), 404
    
    #regresamos una respuesta con los resultasos de la consulta 
    response_body = {

        "msg": "Hello, These are your favorites",
        "results": results
    }

    return jsonify(response_body), 200

"""-----------------------------------------------_ </Favoritos> _--------------------------------------"""

"""-----------------------------------------------_<Usuatio/Favorito>_-----------------------------------------"""

""" @app.route('/favoritos', methods=['GET'])
def get_favoritos():

    #hacemos una consulta a la tabla planetas para que traiga todos los registros
    favoritos_querys = Favoritos.query.all()

    #mapeamos para convertir el array [<Planetas 1>] => un array de objetos
    results = list (map(lambda item: item.serialize(),favoritos_querys))

    # control de error para array vacio
    if results == []:
        return jsonify({"msg": "No hay favorites"}), 404
    
    #regresamos una respuesta con los resultasos de la consulta 
    response_body = {

        "msg": "Hello, These are your favorites",
        "results": results
    }

    return jsonify(response_body), 200 """

"""-----------------------------------------------_ </Usuatio/Favorito> _--------------------------------------"""


# Original mgs /user
@app.route('/user/', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

"""-----------------------------------------------------------------------------------_</GIT ALL>_-------------------------------------------------------------"""


"""-----------------------------------------------------------------------------------_<GIT Espesifico>_-------------------------------------------------------------"""

"""-----------------------------------------------_<One_personaje>_------------------------------------------"""

@app.route('/personajes/<int:personaje_id>', methods=['GET'])
def get_one_personaje(personaje_id):
    
    print(personaje_id)
    #hacemos una consulta a la tabla planetas para que traiga todos los registros
    personajes_querys = Personajes.query.filter_by(id = personaje_id).first()
    
    # si el resultado es vacio respondemos que no hay planetas

    if personajes_querys is None:
          return jsonify({"msg": "No hay personajes"}), 404

    
    #regresamos una respuesta con los resultasos de la consulta 
    response_body = {

        "msg": "Hello, These are your personajes ",
        "results": personajes_querys.serialize()
    }

    return jsonify(response_body), 200


"""-----------------------------------------------_</One_personaje>_------------------------------------------"""


"""-----------------------------------------------_<One_Planeta>_------------------------------------------"""

@app.route('/planetas/<int:planet_id>', methods=['GET'])
def get_one_planetas(planet_id):
    
    print(planet_id)
    #hacemos una consulta a la tabla planetas para que traiga todos los registros
    planetas_querys = Planetas.query.filter_by(id = planet_id).first()
    
    # si el resultado es vacio respondemos que no hay planetas

    if planetas_querys is None:
          return jsonify({"msg": "No hay planetas"}), 404

    
    #regresamos una respuesta con los resultasos de la consulta 
    response_body = {

        "msg": "Hello, These are your planets ",
        "results": planetas_querys.serialize()
    }

    return jsonify(response_body), 200
"""-----------------------------------------------_</One_Planeta>_------------------------------------------"""


"""-----------------------------------------------_<One_Vehiculo>_------------------------------------------"""

@app.route('/vehiculos/<int:vehiculos_id>', methods=['GET'])
def get_one_vehiculos(vehiculos_id):
    
    print(vehiculos_id)
    #hacemos una consulta a la tabla planetas para que traiga todos los registros
    vehiculos_querys = Vehiculos.query.filter_by(id = vehiculos_id).first()
    
    # si el resultado es vacio respondemos que no hay planetas

    if vehiculos_querys is None:
          return jsonify({"msg": "No hay vehiculo"}), 404

    
    #regresamos una respuesta con los resultasos de la consulta 
    response_body = {

        "msg": "Hello, These are your vehicle ",
        "results": vehiculos_querys.serialize()
    }

    return jsonify(response_body), 200
"""-----------------------------------------------_</One_Vehiculo>_------------------------------------------"""


"""-----------------------------------------------_<One_Starships>_------------------------------------------"""

@app.route('/starships/<int:starships_id>', methods=['GET'])
def get_one_starships(starships_id):
    
    print(starships_id)
    #hacemos una consulta a la tabla planetas para que traiga todos los registros
    starships_querys = Starships.query.filter_by(id = starships_id).first()
    
    # si el resultado es vacio respondemos que no hay planetas

    if starships_querys is None:
          return jsonify({"msg": "No hay starships"}), 404

    
    #regresamos una respuesta con los resultasos de la consulta 
    response_body = {

        "msg": "Hello, These are your starships ",
        "results": starships_querys.serialize()
    }

    return jsonify(response_body), 200
"""-----------------------------------------------_</One_Starships>_------------------------------------------"""

"""-----------------------------------------------_<One_Usuario>_------------------------------------------"""

@app.route('/usuario/<int:usuario_id>', methods=['GET'])
def get_one_usuario(usuario_id):
    
    print(usuario_id)
    #hacemos una consulta a la tabla planetas para que traiga todos los registros
    usuario_querys = Usuario.query.filter_by(id = usuario_id).first()
    
    # si el resultado es vacio respondemos que no hay planetas

    if usuario_querys is None:
          return jsonify({"msg": "No hay usuario"}), 404

    
    #regresamos una respuesta con los resultasos de la consulta 
    response_body = {

        "msg": "Hello, These are your user ",
        "results": usuario_querys.serialize()
    }

    return jsonify(response_body), 200
"""-----------------------------------------------_</One_Usuario>_------------------------------------------"""

"""-----------------------------------------------_<One_Favoritos>_------------------------------------------"""

@app.route('/favoritos/<int:favoritos_id>', methods=['GET'])
def get_one_favoritos(favoritos_id):
    
    print(favoritos_id)
    #hacemos una consulta a la tabla planetas para que traiga todos los registros
    favoritos_querys = Favoritos.query.filter_by(id = favoritos_id).first()
    
    # si el resultado es vacio respondemos que no hay planetas

    if favoritos_querys is None:
          return jsonify({"msg": "No hay favoritos"}), 404

    
    #regresamos una respuesta con los resultasos de la consulta 
    response_body = {

        "msg": "Hello, These are your favorite ",
        "results": favoritos_querys.serialize()
    }

    return jsonify(response_body), 200
"""-----------------------------------------------_</One_Favoritos>_------------------------------------------"""

"""-----------------------------------------------------------------------------------_</GIT Espesifico>_-------------------------------------------------------------"""


"""-----------------------------------------------------------------------------------_<POST>_-------------------------------------------------------------"""


"""-----------------------------------------------_</POST_Favoritos>_------------------------------------------"""

@app.route('/personajes', methods=['POST'])

def create_personaje():
    request_body = json.loads(request.data)

    existing_personaje = Personajes.query.filter_by(**request_body).first()

    if existing_personaje:
        return jsonify({"message": "El personaje ya existe"}), 400

    new_personaje = Personajes(**request_body)
    db.session.add(new_personaje)
    db.session.commit()
    
    return jsonify(new_personaje.serialize()), 200

"""-----------------------------------------------------------------------------------_</POST>_-------------------------------------------------------------"""




"""----------------------------------------------------------------------------------------------------empoints - JMartinez------------------------------------------------------------ """



 

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)

