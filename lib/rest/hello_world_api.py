import logging

from flask_headers import headers

from lib.rest import hello_bp


@headers(
    headerDict={
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': 'true'
    })
@hello_bp.route("/", methods=["GET"])
def get():
    logging.info(f"Saying hello")
    return {'hello': 'world'}


@headers(
    headerDict={
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': 'true'
    })
@hello_bp.route("/lightsabers", methods=["GET"])
def lightsabers():
    logging.info(f"Fetching all the lightsaber colors")
    return [
        "purple",
        "green",
        "yellow",
        "blue",
        "red",
        "black",
        "white",
        "light blue"
    ]
