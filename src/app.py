from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:password@localhost/flask_challenge'
app.config['SQLALCHEMY_RACK_MODIFICATIONS']=False

database = SQLAlchemy(app)
marshmallow = Marshmallow(app)

class User(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    email = database.Column(database.String(35), unique=True)
    password = database.Column(database.String(250))
    name = database.Column(database.String(80))

    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name

database.create_all()

class UserSchema(marshmallow.Schema):
    class Meta:
        fields = ('id', 'email', 'password', 'name')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

@app.route('/users', methods=['POST'])
def create_user():
    email = request.json['email']
    password = request.json['password']
    name = request.json['name']

    new_user = User(email, password, name)
    
    database.session.add(new_user)
    database.session.commit()
    
    return user_schema.jsonify(new_user)


@app.route('/users', methods=['GET'])
def get_users():
    all_users = User.query.all()
    list_of_all_users = users_schema.dump(all_users)
    return jsonify(list_of_all_users)

if __name__ == '__main__':
    app.run(debug=True)