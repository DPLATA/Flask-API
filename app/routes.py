from flask import request, jsonify
from app import app, database
from app.models import User, users_schema, user_schema, Address

@app.route('/users', methods=['POST'])
def create_user():
    email = request.json['email']
    password = request.json['password']
    name = request.json['name']

    # TODO: hash password
    new_user = User(email, password, name)
    
    database.session.add(new_user)
    database.session.commit()
    
    return user_schema.jsonify(new_user)


@app.route('/users', methods=['GET'])
def get_users():
    all_users = User.query.all()
    # list_of_all_users = users_schema.dump(all_users)
    return user_schema.jsonify(all_users)

@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)

@app.route('/users/<id>/addresses', methods=['POST'])
def create_address(id):
    zip_code = request.json['zip_code']
    municipality = request.json['municipality']
    city = request.json['city']
    state = request.json['state']
    country = request.json['country']
    user_id = id
    # print(user_id)

    new_address = Address(zip_code, municipality, city, state, country, user_id)
    
    database.session.add(new_address)
    database.session.commit()
    
    return user_schema.jsonify(new_address)