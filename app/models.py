from app import database
from app import marshmallow
import datetime

class Base(database.Model):
    __abstract__  = True

    id = database.Column(database.Integer, primary_key=True)
    date_created = database.Column(database.DateTime,  default=database.func.current_timestamp())
    # date_modified = database.Column(database.DateTime,  default=database.func.current_timestamp(), onupdate=database.func.current_timestamp())

class User(Base):
    __tablename__ = 'user'
    
    email = database.Column(database.String(35), unique=True, nullable=False)
    password = database.Column(database.String(60), nullable=False)
    name = database.Column(database.String(80), nullable=False)
    # TODO: addresses = database.relationship('Address', backpopulates='user')

    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name
        self.date_created = datetime.datetime.now()


class UserSchema(marshmallow.Schema):
    class Meta:
        fields = ('id', 'email', 'password', 'name', 'date_created')

class Address(Base):
    __tablename__ = 'address'

    zip_code = database.Column(database.String(35), unique=False, nullable=False)
    municipality = database.Column(database.String(40), nullable=False)
    city = database.Column(database.String(60), nullable=False)
    state = database.Column(database.String(80))
    country = database.Column(database.String(20), nullable=False)
    user_id = database.Column(database.Integer, database.ForeignKey('user.id'))
    # TODO: user = database.relationship('User', back_populates='address')

    def __init__(self, zip_code, municipality, city, state, country, user_id):
        self.zip_code = zip_code
        self.municipality = municipality
        self.city = city
        self.state = state
        self.country = country
        self.date_created = datetime.datetime.now()
        self.user_id = user_id

class AddressSchema(marshmallow.Schema):
    class Meta:
        fields = ('id', 'zip_code', 'municipality', 'city', 'state', 'country', 'date_created', 'user_id')
        # fields = ('id', 'zip_code', 'municipality', 'city', 'state', 'country', 'user_id')

database.create_all()

user_schema = UserSchema()
users_schema = UserSchema(many=True)

address_schema = AddressSchema()
addresses_schema = AddressSchema(many=True)