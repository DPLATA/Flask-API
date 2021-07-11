from flask import request, jsonify
from app import app, database
from app.models import User, users_schema, user_schema

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

@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)