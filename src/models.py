from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# roles_users = db.Table('roles_users',
#    db.Column('roles_id', db.Integer, db.ForeignKey('roles.id'), primary_key=True),
#    db.Column('users_id', db.Integer, db.ForeignKey('users.id'), primary_key=True)
# )

# class Role(db.Model):
#     __tablename__ = 'roles'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), unique=True, nullable=False)
#     is_active = db.Column(db.Boolean(), default=True)
#     users = db.relationship('User', secondary=roles_users)

#     def serialize(self):
#         return {
#             "id": self.id,
#             "name": self.name,
#             "is_active": self.is_active    
#         }

Favorites_People = db.Table('Favorites_People',
   db.Column('people_id', db.Integer, db.ForeignKey('People.id'), primary_key=True),
   db.Column('users_id', db.Integer, db.ForeignKey('User.id'), primary_key=True)
)

Favorites_vehicles = db.Table('Favorites_vehicles',
   db.Column('vehicles_id', db.Integer, db.ForeignKey('Vehicles.id'), primary_key=True),
   db.Column('users_id', db.Integer, db.ForeignKey('User.id'), primary_key=True)
)

Favorites_planets = db.Table('Favorites_planets',
   db.Column('planets_id', db.Integer, db.ForeignKey('Planets.id'), primary_key=True),
   db.Column('users_id', db.Integer, db.ForeignKey('User.id'), primary_key=True)
)


class User(db.Model):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False,)
    email = db.Column(db.String(100), nullable=False, unique=True)
    # name = db.Column(db.String(100), )
    # last_name = db.Column(db.String(100), )
    people = db.relationship('People', secondary="Favorites_People") # [<Role 1>, <Role 2>]
    planets = db.relationship('Planets', secondary="Favorites_planets") # [<Role 1>, <Role 2>]
    vehicles = db.relationship('Vehicles', secondary="Favorites_vehicles") # [<Role 1>, <Role 2>]
    

    def serialize(self):
        return {
            "id": self.id,
            "user_name": self.user_name,
            "email": self.email,
            # "name": self.name,
            # "last_name": self.last_name,
            "people": self.get_people(),
            "planets": self.get_planets(),
            "vehicles": self.get_vehicles()    
        }

    def get_people(self):
        return list(map(lambda person: person.serialize(), self.people)) # []
    def get_planets(self):
        return list(map(lambda planet: planet.serialize(), self.planets)) # []
    def get_vehicles(self):
        return list(map(lambda vehicle: vehicle.serialize(), self.vehicles)) # []


    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class People(db.Model):
    __tablename__ = 'People'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100), nullable=False, unique=True)
    # height = db.Column(db.Integer, nullable=False,)
    # mass = db.Column(db.Integer, nullable=False,)
    # hair_color = db.Column(db.String(100), )
    # skin_color = db.Column(db.String(100), )
    # eye_color = db.Column(db.String(100), )
    # birth_year = db.Column(db.String(100), )
    # gender = db.Column(db.String(100), )
    users = db.relationship('User', secondary=Favorites_People)

    def serialize(self):
        return {
            "id": self.id,
            "Name": self.Name,
            # "height": self.height,
            # "mass": self.mass,
            # "hair_color": self.hair_color,
            # "skin_color": self.skin_color,
            # "eye_color": self.eye_color,
            # "birth_year": self.birth_year,
            # "gender": self.gender,

        }
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Planets(db.Model):
    __tablename__ = 'Planets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100), nullable=False, unique=True)
    # rotation_period = db.Column(db.Integer, nullable=False,)
    # orbital_period = db.Column(db.Integer, nullable=False,)
    # diameter = db.Column(db.Integer, nullable=False,)
    # climate = db.Column(db.String(100), )
    # gravity = db.Column(db.String(100), )
    # terrain = db.Column(db.String(100), )
    # surface_water = db.Column(db.Integer, nullable=False,)

    def serialize(self):
        return {
            "id": self.id,
            "Name": self.Name,
            # "rotation_period": self.rotation_period,
            # "orbital_period": self.orbital_period,
            # "diameter": self.diameter,
            # "climate": self.climate,
            # "gravity": self.gravity,
            # "terrain": self.terrain,
            # "surface_water": self.surface_water,
        }
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Vehicles(db.Model):
    __tablename__ = 'Vehicles'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100), nullable=False, unique=True)
    # model = db.Column(db.String(100), )
    # manufacturer = db.Column(db.String(100), )
    # cost_in_credits = db.Column(db.Integer, nullable=False,)
    # length = db.Column(db.Integer, nullable=False,)
    # max_atmosphering_speed = db.Column(db.Integer, nullable=False,)
    # crew = db.Column(db.Integer, nullable=False,)
    # passengers = db.Column(db.Integer, nullable=False,)

    def serialize(self):
        return {
            "id": self.id,
            "Name": self.Name,
            # "model": self.model,
            # "manufacturer": self.manufacturer,
            # "cost_in_credits": self.cost_in_credits,
            # "length": self.length,
            # "max_atmosphering_speed": self.max_atmosphering_speed,
            # "crew": self.crew,
            # "passengers": self.passengers,
        }
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


# class Favorites_People(db.Model):
#     __tablename__ = 'Favorites_people'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.


#     people_id = db.Column(db.Integer, db.ForeignKey('People.id'), primary_key=True)
#     users_id = db.Column(db.Integer, db.ForeignKey('User.id'),nullable=False, primary_key=True)


#     def serialize(self):
#         return {

#             "people_id": self.people_id,
#             "users_id": self.users_id,

#         }

# class Favorites_planets(db.Model):
#     __tablename__ = 'Favorites_planets'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.

#     id = db.Column(db.Integer, db.ForeignKey('User.id'), primary_key=True)
#     planets_id = db.Column(db.Integer, db.ForeignKey('Planets.id'))

#     def serialize(self):
#         return {
#             "id": self.id,
#             "planets_id": self.planets_id,
#         }

# class Favorites_vehicles(db.Model):
#     __tablename__ = 'Favorites_vehicles'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.

#     id = db.Column(db.Integer, db.ForeignKey('User.id'), primary_key=True)
#     vehicles_id = db.Column(db.Integer, db.ForeignKey('Vehicles.id'))

#     def serialize(self):
#         return {
#             "id": self.id,
#             "vehicles_id": self.vehicles_id,
#         }