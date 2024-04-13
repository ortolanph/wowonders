from flask import Blueprint

hello_bp: Blueprint = Blueprint('hello', __name__, )
from lib.rest import hello_world_api

wow_bp: Blueprint = Blueprint('wow', __name__, )
from lib.rest import wow_api
