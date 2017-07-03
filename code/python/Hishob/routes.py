from flask import jsonify
from flask import render_template
from flask import flash
from flask import current_app
from flask import abort

from middleware import user
from middleware import user_by_id
from middleware import add_user
from middleware import initialize_database as init_db
from middleware import fill_database as fill_db
from middleware import build_message

def init_api_routes(app):
    if app:
        app.add_url_rule('/api/user/<string:id>', 'user_by_id', user_by_id, methods=['GET'])
        app.add_url_rule('/api/user/', 'user', user, methods=['GET'])
        app.add_url_rule('/api/user/', 'add_user', add_user, methods=['POST'])
        app.add_url_rule('/api/initdb', 'initdb', initialize_database)
        app.add_url_rule('/api/filldb', 'filldb', fill_database)
        app.add_url_rule('/api', 'list_routes', list_routes, methods=['GET'], defaults={'app': app})

def initialize_database():
    message_key = "Initialize Database"
    try:
        init_db()
    except ValueError as err:
        return jsonify(build_message(message_key, err.message))
    
    return jsonify(build_message(message_key, "OK"))

def fill_database():
    message_key = "Fill Database"
    try:
        fill_db()
    except ValueError as err:
        return jsonify(build_message(message_key, err.message))

    return jsonify(build_message(message_key, "OK"))

def list_routes(app):
    result = []
    for rt in app.url_map.iter_rules():
        result.append({
            'methods': list(rt.methods),
            'route': str(rt)
        })
    return jsonify({'routes': result, 'total': len(result)})
