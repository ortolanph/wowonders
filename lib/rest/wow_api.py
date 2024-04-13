import logging

from flask_headers import headers

from lib.rest import wow_bp
from lib.service.wow_service import WOWService


@headers(
    headerDict={
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': 'true'
    })
@wow_bp.route("/wow/v1/stages/<country>", methods=["GET"])
def get_stage_by_country(country: str):
    raise NotImplementedError("get_stage_by_country is not implemented")


@headers(
    headerDict={
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': 'true'
    })
@wow_bp.route("/wow/v1/stages/<landmark>", methods=["GET"])
def get_stage_by_landmark(landmark: str):
    raise NotImplementedError("get_stage_by_landmark is not implemented")


@headers(
    headerDict={
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': 'true'
    })
@wow_bp.route("/wow/v1/stages/<expr>/search", methods=["GET"])
def search_stage(expr: str):
    raise NotImplementedError("search_stage is not implemented")


@headers(
    headerDict={
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': 'true'
    })
@wow_bp.route("/wow/v1/level/<words>", methods=["GET"])
def search_level_by_words(words: str):
    raise NotImplementedError("search_level_by_words is not implemented")


@headers(
    headerDict={
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': 'true'
    })
@wow_bp.route("/wow/v1/answers/<level_id>", methods=["GET"])
def get_answers(level_id: int):
    logging.info(f"Saying hello")
    service = WOWService()

    level_data = service.load_level_data(level_id)
    level_answers = service.load_answers(level_id)
    level_data["level_info"]["answers"] = level_answers

    return level_data
