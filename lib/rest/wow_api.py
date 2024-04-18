import logging

from flask_headers import headers

from lib.rest import wow_bp
from lib.service.wow_service import WOWService


# TODO: Implement this method
@headers(
    headerDict={
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': 'true'
    })
@wow_bp.route("/wow/v1/stages/country/<country>", methods=["GET"])
def get_stages_by_country(country: str):
    logging.info(f"Retrieving stage data from stage which country is like {country}")
    service = WOWService()

    return service.get_stages_by_country(country)


# TODO: Implement this method
@headers(
    headerDict={
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': 'true'
    })
@wow_bp.route("/wow/v1/stages/landmark/<landmark>", methods=["GET"])
def get_stages_by_landmark(landmark: str):
    raise NotImplementedError("get_stage_by_landmark is not implemented")


# TODO: Implement this method
@headers(
    headerDict={
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': 'true'
    })
@wow_bp.route("/wow/v1/stages/search/<expr>", methods=["GET"])
def search_stage(expr: str):
    raise NotImplementedError("search_stage is not implemented")


# TODO: Implement this method
@headers(
    headerDict={
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': 'true'
    })
@wow_bp.route("/wow/v1/levels/<words>", methods=["GET"])
def search_levels_by_words(words: str):
    raise NotImplementedError("search_level_by_words is not implemented")


@headers(
    headerDict={
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': 'true'
    })
@wow_bp.route("/wow/v1/answers/<level_id>", methods=["GET"])
def get_answers(level_id: int):
    logging.info(f"Retrieving answers from level {level_id}")
    service = WOWService()

    level_data = service.load_level_data(level_id)
    level_answers = service.load_answers(level_id)
    level_data["level_info"]["answers"] = level_answers

    return level_data
