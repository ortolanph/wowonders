import logging

from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from lib.rest import hello_bp, wow_bp

logging.basicConfig(
    level=logging.INFO,
)

appName = "Activation Service Mock in Python"

app = Flask(appName)
CORS(app, support_credentials=True, origins="http://localhost:4200")
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['Access-Control-Allow-Origin'] = '*'
app.config['Access-Control-Allow-Credentials'] = 'true'
app.register_blueprint(hello_bp)
app.register_blueprint(wow_bp)

api = Api(app)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
