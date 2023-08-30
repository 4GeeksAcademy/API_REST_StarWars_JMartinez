from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()

class User(db.Model):

    id          = db.Column(db.Integer, primary_key=True)
    email       = db.Column(db.String(120), unique=True, nullable=False)
    password    = db.Column(db.String(80), unique=False, nullable=False)
    is_active   = db.Column(db.Boolean(), unique=False, nullable=False)


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

    def __repr__(self):
        return '<Personajes %r>' % self.id

    def serialize(self):
        return {
            "id"            :self.id,
            "name"          :self.name,
            "mass"          :self.mass,
            "hair_color"    :self.hair_color,
            "skin_color"    :self.skin_color,
            "eye_color"     :self.eye_color,
            "birth_year"    :self.birth_year,
            "height"        :self.height,
            "gender"        :self.gender 
        }

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

    def __repr__(self):
        return '<Planetas %r>' % self.id

    def serialize(self):
        return {
            "id"                :self.id,
            "name"              :self.name,
            "diameter"          :self.diameter,
            "rotation_period"   :self.rotation_period,
            "orbital_period"    :self.orbital_period,
            "gravity"           :self.gravity,
            "population"        :self.population,
            "climate"           :self.climate,
            "terrain"           :self.terrain,
            "surface_water"     :self.surface_water           
        }
    
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


    def __repr__(self):
        return '<Vehiculos %r>' % self.id

    def serialize(self):
        return {
            "id"                    :self.id,
            "name"                  :self.name,
            "model"                 :self.model,
            "vehicle_class"         :self.vehicle_class,
            "manufacturer"          :self.manufacturer,
            "cost_in_credits"       :self.cost_in_credits,
            "length"                :self.length,
            "crew"                  :self.crew,
            "max_atmosphering_speed":self.max_atmosphering_speed,
            "cargo_capacity"        :self.cargo_capacity,
            "consumables"           :self.consumables,
            "films"                 :self.films,
            "pilots"                :self.pilots,
          
          
        }


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


    def __repr__(self):
        return '<Starships %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name":self.name,
            "model":self.model,
            "starship_class":self.starship_class,
            "manufacturer":self.manufacturer,
            "cost_in_credits":self.cost_in_credits,
            "manufacturer":self.manufacturer,
            "length":self.length,
            "crew":self.crew,
            "passengers":self.passengers,
            "max_atmosphering_speed":self.max_atmosphering_speed,
            "cargo_capacity":self.cargo_capacity,
            "consumables":self.consumables,
            "films":self.films,
            "pilots":self.pilots,
            "hyperdrive_rating":self.hyperdrive_rating,
            "MGLT":self.MGLT
        }

class Usuario(db.Model):

    id            = db.Column(db.Integer, primary_key=True)
    name          = db.Column(db.String(120), nullable=False)
    last_name     = db.Column(db.String(120), nullable=False)
    email         = db.Column(db.String(120), nullable=False)
    password      = db.Column(db.String(120), nullable=False)
    Fech_subscrip = db.Column(db.String(120), nullable=False)
    Activo        = db.Column(db.String(120), nullable=False)


    def __repr__(self):
        return '<Usuario %r>' % self.id

    def serialize(self):
        return {

            "id": self.id,
            "name":self.name,
            "last_name":self.last_name,
            "email":self.email,
            "password":self.password,
            "Fech_subscrip":self.Fech_subscrip,
            "Activo":self.Activo
            # do not serialize the password, its a security breach
        }

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
        return '<Favoritos %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "personaje_id":self.personaje_id,
            "vehiculo_id ":self.vehiculo_id,
            "planeta_id  ":self.planeta_id,
            "usuario_id  ":self.usuario_id,
            "starships_id":self.starships_id
          
            # do not serialize the password, its a security breach
    }   