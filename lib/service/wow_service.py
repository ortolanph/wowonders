import logging

from lib.crawler.wow_crawler import Crawler
from lib.data.wow_repository import WOWRepository


class WOWService:
    _crawler = None
    _repository = None

    def __init__(self):
        logging.info("Init Crawler")
        self._crawler = Crawler()
        logging.info("Init Repository")
        self._repository = WOWRepository()

    def retrieve_data(self):
        logging.info("Retrieving data")
        self._crawler.crawl()

        while self._crawler.has_next():
            self._crawler.next()

            stage = self._crawler.current()

            if not self._repository.is_stage_processed(stage.country, stage.landmark):
                logging.info(f"Inserting stage {stage.country}/{stage.landmark} at the database")

                if not self._repository.exist_stage(stage.country, stage.landmark):
                    self._repository.insert_stage(stage.country, stage.landmark)

                stage_id = self._repository.get_stage_id(stage.country, stage.landmark)
                stage = self._crawler.current_stage()

                for level in stage.levels:
                    logging.info(f"Inserting level {level.level_number} at the database")

                    if not self._repository.exist_level(level.level_number):
                        self._repository.insert_level(stage_id, level.level_number, level.letters)

                    level_id = self._repository.get_level_id(level.level_number)

                    for answer in level.answers:
                        logging.info(f"Inserting answer {answer} at the database")

                        if not self._repository.exist_answer(answer):
                            self._repository.insert_answer(answer)

                        answer_id = self._repository.get_answer_id(answer)
                        self._repository.link_level_to_answer(level_id, answer_id)

                self._repository.mark_as_processed(stage_id)

    def load_stage_data(self):
        logging.info("Fetching stage data")
        return self._repository.get_stages()

    def load_levels(self, stage_id):
        logging.info(f"Fetching levels from stage {stage_id}")
        return self._repository.get_levels(stage_id)

    def load_answers(self, level_id):
        logging.info(f"Fetching answers for level {level_id}")
        return self._repository.get_answers(level_id)

    def load_level_data(self, level_id):
        logging.info(f"Fetching level data for level {level_id}")
        return self._repository.get_level_data(level_id)

    def get_stages_by_country(self, country):
        logging.info(f"Fetching stages by Country {country}")
        stages = self._repository.get_stages_by_country(country)
        stages_ids = list(map(lambda stage: stage[0], stages))
        level_infos = self._repository.get_levels_by_stages(stages_ids)
        level_info_resources = list(
            map(
                lambda level_info: {"stage_id": level_info[0], "level_resource": f"/wow/v1/answers/{level_info[1]}"},
                level_infos
            )
        )
        
        formatted_data = list(
            map(
                lambda stage: {
                    "id": stage[0],
                    "country": stage[1],
                    "landmark": stage[2],
                    "levels": [
                        level_info["level_resource"]
                        for level_info in level_info_resources
                        if level_info["stage_id"] == stage[0]
                    ]}, stages
            )
        )

        return formatted_data

    def load_interval_levels(self, from_level_id, to_level_id):
        levels = []
        for level in range(int(from_level_id), int(to_level_id) + 1):
            level_info = self.load_level_data(level)
            level_info["level_info"]["answers"] = self.load_answers(level)
            level_info["level_info"]["answers_string"] = ", ".join(level_info["level_info"]["answers"])
            levels.append(level_info)

        return levels
