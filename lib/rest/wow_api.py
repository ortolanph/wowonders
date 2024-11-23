import logging

from flask import Response
from flask_headers import headers

from lib.reporter.wow_reporter import fill_template
from lib.rest import wow_bp
from lib.service.wow_service import WOWService


# TODO: Implement this method
@headers(
    headerDict={
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': 'true'
    })
@wow_bp.route("/v1/wow/stages/country/<country>", methods=["GET"])
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
@wow_bp.route("/v1/wow/stages/landmark/<landmark>", methods=["GET"])
def get_stages_by_landmark(landmark: str):
    raise NotImplementedError("get_stage_by_landmark is not implemented")


# TODO: Implement this method
@headers(
    headerDict={
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': 'true'
    })
@wow_bp.route("/v1/wow/stages/search/<expr>", methods=["GET"])
def search_stage(expr: str):
    raise NotImplementedError("search_stage is not implemented")


# TODO: Implement this method
@headers(
    headerDict={
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': 'true'
    })
@wow_bp.route("/v1/wow/levels/<words>", methods=["GET"])
def search_levels_by_words(words: str):
    raise NotImplementedError("search_level_by_words is not implemented")


@headers(
    headerDict={
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': 'true'
    })
@wow_bp.route("/v1/wow/answers/<level_id>", methods=["GET"])
def get_answers(level_id: int):
    logging.info(f"Retrieving answers from level {level_id}")
    service = WOWService()

    level_data = service.load_level_data(level_id)
    level_answers = service.load_answers(level_id)
    level_data["level_info"]["answers"] = level_answers

    return level_data


@headers(
    headerDict={
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': 'true'
    })
@wow_bp.route("/v1/wow/answers/from/<from_level_id>/to/<to_level_id>", methods=["GET"])
def get_answers_from_level_to_level(from_level_id: int, to_level_id: int):
    logging.info(f"Retrieving answers from level {from_level_id} to {to_level_id}")
    service = WOWService()

    level_data = service.load_interval_levels(from_level_id, to_level_id)
    pdf = fill_template(level_data)

    return Response(
        pdf,
        mimetype='application/pdf',
        headers={"Content-Disposition": "inline; filename=report.pdf"}
    )
