from flask import jsonify
from flask import abort
from flask import make_response
from flask import request
from flask import url_for

from data_provider_service import DataProviderService

db_engine = 'mysql+pymysql://root:root@localhost/hishob_python'

DATA_PROVIDER = DataProviderService(db_engine)

def user(serialize = True):
    users = DATA_PROVIDER.get_user(serialize=serialize)
    if serialize:
        return jsonify({"users" : users, "total" : len(users)})
    else:
        return users

def user_by_id(id):
    current_user = DATA_PROVIDER.get_user(id, serialize=True)
    if current_user:
        return jsonify({"user" : current_user})
    else:
        abort(404)

def initialize_database():
    DATA_PROVIDER.init_database()

def fill_database():
    DATA_PROVIDER.fill_database()

def add_user():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    middle_name = request.form["middle_name"]
    user_name = request.form["user_name"]
    email = request.form["email"]
    mobile_number = request.form["mobile_number"]

    new_user_id = DATA_PROVIDER.add_user(first_name=first_name,
                                         last_name=last_name, middle_name=middle_name, user_name=user_name, email=email, mobile_number=mobile_number)
    
    return jsonify({
        "user_id" : new_user_id,
        "url" : url_for("user_by_id", id=new_user_id)
    })

def build_message(key, message):
    return {key:message}