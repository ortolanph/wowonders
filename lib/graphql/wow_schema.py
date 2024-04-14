from graphene import ObjectType, String, Schema, Int, List, Field

from lib.service.wow_service import WOWService


def _get_level_data(level_id: int):
    service = WOWService()

    level_data = service.load_level_data(level_id)
    level_answers = service.load_answers(level_id)
    level_data["level_info"]["answers"] = level_answers

    return level_data


class LevelInfo(ObjectType):
    level_id = Int()
    level_letters = String()
    answers = List(String)


class StageInfo(ObjectType):
    stage_id = Int()
    stage_country = String()
    stage_landmark = String()


class LevelAnswersResponse(ObjectType):
    level_info = Field(LevelInfo)
    stage_info = Field(StageInfo)


class Query(ObjectType):
    hello = String(first_name=String(required=True))
    level_answers = Field(LevelAnswersResponse, level_id=Int())

    def resolve_hello(self, info, first_name):
        return f"Hello {first_name}"

    def resolve_level_answers(self, info, level_id):
        data = _get_level_data(level_id)

        stage_info = StageInfo(
            stage_id=data["stage_info"]["stage_id"],
            stage_country=data["stage_info"]["stage_country"],
            stage_landmark=data["stage_info"]["stage_landmark"],
        )

        level_info = LevelInfo(
            level_id=data["level_info"]["level_id"],
            level_letters=data["level_info"]["level_letters"],
            answers=data["level_info"]["answers"],
        )

        return LevelAnswersResponse(
            stage_info=stage_info,
            level_info=level_info
        )


schema = Schema(
    query=Query,
    types=[LevelInfo, StageInfo, LevelAnswersResponse]
)
