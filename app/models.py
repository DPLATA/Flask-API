from app import database
from app import marshmallow

class User(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    email = database.Column(database.String(35), unique=True, nullable=False)
    password = database.Column(database.String(250), nullable=False)
    name = database.Column(database.String(80), nullable=False)

    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name


class UserSchema(marshmallow.Schema):
    class Meta:
        fields = ('id', 'email', 'password', 'name')

database.create_all()

user_schema = UserSchema()
users_schema = UserSchema(many=True)