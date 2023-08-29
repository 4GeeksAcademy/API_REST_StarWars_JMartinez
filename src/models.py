from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base


db = SQLAlchemy()

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)


class Personajes(db.Model):

    id          = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String(120),  nullable=False)
    mass        = db.Column(db.String(120),  nullable=False)
    hair_color	= db.Column(db.String(120),  nullable=False)
    skin_color	= db.Column(db.String(120),  nullable=False)
    eye_color	= db.Column(db.String(120),  nullable=False)
    birth_year	= db.Column(db.String(120),  nullable=False)
    height      = db.Column(db.String(120),  nullable=False)
    gender	    = db.Column(db.String(120),  nullable=False)


class Planetas(db.Model): 

    id              = db.Column(db.Integer, primary_key=True)
    name            = db.Column(db.String(120), nullable=False)
    diameter        = db.Column(db.String(120), nullable=False)
    rotation_period	= db.Column(db.String(120), nullable=False)
    orbital_period	= db.Column(db.String(120), nullable=False)
    gravity	        = db.Column(db.String(120), nullable=False)
    population	    = db.Column(db.String(120), nullable=False)
    climate	        = db.Column(db.String(120), nullable=False)
    terrain         = db.Column(db.String(120), nullable=False)
    surface_water   = db.Column(db.String(120), nullable=False)


class Vehiculos(db.Model):
  
    id                      = db.Column(db.Integer, primary_key=True)
    name                    = db.Column(db.String(120), nullable=False)
    model                   = db.Column(db.String(120), nullable=False)
    vehicle_class	        = db.Column(db.String(120), nullable=False)
    manufacturer	        = db.Column(db.String(120), nullable=False)
    cost_in_credits	        = db.Column(db.Integer(), nullable=False)
    length	                = db.Column(db.Integer(), nullable=False)
    crew	                = db.Column(db.Integer(), nullable=False)
    max_atmosphering_speed  = db.Column(db.Integer(), nullable=False)
    cargo_capacity          = db.Column(db.Integer(), nullable=False)
    consumables             = db.Column(db.String(120), nullable=False)
    films                   = db.Column(db.Integer(), nullable=False)
    pilots                  = db.Column(db.Integer(), nullable=False)


class Starships(db.Model):
    
    id                      = db.Column(db.Integer, primary_key=True)
    name                    = db.Column(db.String(120), nullable=False)
    model                   = db.Column(db.String(120), nullable=False)
    starship_class	        = db.Column(db.String(120), nullable=False)
    manufacturer	        = db.Column(db.String(120), nullable=False)
    cost_in_credits	        = db.Column(db.Integer(), nullable=False)
    length	                = db.Column(db.Integer(), nullable=False)
    crew	                = db.Column(db.Integer(), nullable=False)
    passengers              = db.Column(db.Integer(), nullable=False)
    max_atmosphering_speed  = db.Column(db.Integer(), nullable=False)
    cargo_capacity          = db.Column(db.Integer(), nullable=False)
    consumables             = db.Column(db.String(120), nullable=False)
    films                   = db.Column(db.Integer(), nullable=False)
    pilots                  = db.Column(db.Integer(), nullable=False)
    hyperdrive_rating       = db.Column(db.Integer(), nullable=False)
    MGLT                    = db.Column(db.Integer(), nullable=False)

class Usuario(db.Model):

    id            = db.Column(db.Integer, primary_key=True)
    name          = db.Column(db.String(120), nullable=False)
    last_name     = db.Column(db.String(120), nullable=False)
    email         = db.Column(db.String(120), nullable=False)
    password      = db.Column(db.String(120), nullable=False)
    Fech_subscrip = db.Column(db.String(120), nullable=False)
    Activo        = db.Column(db.String(120), nullable=False)

class Favoritos(db.Model):
   
    id            = db.Column(db.Integer, primary_key=True)
    personaje_id  = db.Column(db.Integer, db.ForeignKey('personajes.id'))
    vehiculo_id   = db.Column(db.Integer, db.ForeignKey('vehiculos.id'))
    planeta_id    = db.Column(db.Integer, db.ForeignKey('planetas.id'))
    usuario_id    = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    starships_id  = db.Column(db.Integer, db.ForeignKey('starships.id'))
    usuario       = db.relationship(Usuario)
    person        = db.relationship(Personajes)
    Vehi          = db.relationship(Vehiculos)
    plane         = db.relationship(Planetas)
    star          = db.relationship(Starships)

    def __repr__(self):
        return '<Favoritos %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            # do not serialize the password, its a security breach
        }