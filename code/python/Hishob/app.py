from flask import Flask

from routes import init_api_routes

#create the flask application
app = Flask(__name__)

app.config['SECRET_KEY'] = 'Hello from Sushank'

init_api_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
