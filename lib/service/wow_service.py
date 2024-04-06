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
