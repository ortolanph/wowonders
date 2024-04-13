""" Database module. """
import logging

from lib.data.wow_connection_manager import ConnectionManager
from lib.data.wow_sql import *


class WOWRepository:
    """ Performs operations in the database """
    _connection = None

    def __init__(self):
        """ Initializes the Movie Repository """
        logging.info("Creating a connection manager")
        manager = ConnectionManager()
        self._connection = manager.get_connection()

    def _close_connection(self):
        """ Closes connection """
        logging.info("Closing connection")
        self._connection.close()
        self._connection = None

    # -------------------------- STAGE --------------------------
    def exist_stage(self, country, landmark):
        logging.info(f"Is stage {country}/{landmark} already registered?")
        cursor = self._connection.execute(COUNT_STAGE, (country, landmark))

        count_stages = cursor.fetchone()[0]

        return count_stages > 0

    def get_stage_id(self, country, landmark):
        logging.info(f"Fetching {country}/{landmark} stage id")
        cursor = self._connection.execute(SELECT_STAGE_ID, (country, landmark))

        wow_stage_id = cursor.fetchone()[0]

        return wow_stage_id

    def insert_stage(self, country, landmark):
        logging.info(f"Inserting stage {country}/{landmark}")
        cursor = self._connection.cursor()

        cursor.execute(INSERT_STAGE, (country, landmark))

        self._connection.commit()

    def is_stage_processed(self, country, landmark):
        logging.info(f"Is {country}/{landmark} stage already processed")
        cursor = self._connection.execute(IS_STAGE_PROCESSED, (country, landmark))

        wow_stage_processed = cursor.fetchone()

        return (False, True)[wow_stage_processed[0]] if wow_stage_processed is not None else False

    def mark_as_processed(self, stage_id):
        logging.info(f"Marking stage {stage_id} as processed")
        cursor = self._connection.cursor()

        cursor.execute(UPDATE_PROCESSED, (stage_id,))

        self._connection.commit()

    # -------------------------- LEVEL --------------------------

    def exist_level(self, level_number):
        logging.info(f"Is level {level_number} already registered?")
        cursor = self._connection.execute(COUNT_LEVEL, (level_number,))

        count_levels = cursor.fetchone()[0]

        return count_levels > 0

    def get_level_id(self, level_number):
        logging.info(f"Fetching {level_number} level id")
        cursor = self._connection.execute(SELECT_LEVEL_ID, (level_number,))

        wow_stage_id = cursor.fetchone()[0]

        return wow_stage_id

    def insert_level(self, stage_id, level_number, level_words):
        logging.info(f"Inserting level {level_number}")
        cursor = self._connection.cursor()

        cursor.execute(INSERT_LEVEL, (stage_id, level_number, level_words))

        self._connection.commit()

    # -------------------------- ANSWER --------------------------

    def exist_answer(self, level_answer):
        logging.info(f"Is answer {level_answer} already registered?")
        cursor = self._connection.execute(COUNT_ANSWER, (level_answer,))

        count_answers = cursor.fetchone()[0]

        return count_answers > 0

    def get_answer_id(self, level_answer):
        logging.info(f"Fetching {level_answer} answer id")
        cursor = self._connection.execute(SELECT_ANSWER_ID, (level_answer,))

        wow_stage_id = cursor.fetchone()[0]

        return wow_stage_id

    def insert_answer(self, level_answer):
        logging.info(f"Inserting answer {level_answer}")
        cursor = self._connection.cursor()

        cursor.execute(INSERT_ANSWER, (level_answer,))

        self._connection.commit()

    # -------------------------- LEVEL X ANSWERS --------------------------

    def link_level_to_answer(self, level_id, answer_id):
        logging.info(f"Linking Level {level_id} to Answer {answer_id} ")
        cursor = self._connection.cursor()

        cursor.execute(LINK_ANSWER_TO_LEVEL, (level_id, answer_id))

        self._connection.commit()

    def get_stages(self):
        logging.info(f"Fetching stage data")
        cursor = self._connection.execute(ALL_STAGES)

        stage_data = {}
        rows = cursor.fetchall()

        for row in rows:
            key = f"{row[1]} - {row[2]}"
            stage_data[key] = row[0]

        return stage_data

    def get_levels(self, stage_id):
        logging.info(f"Fetching stage levels from stage {stage_id}")
        cursor = self._connection.execute(LEVEL_BY_STAGE_ID, (stage_id,))

        level_data = {}
        rows = cursor.fetchall()

        for row in rows:
            key = f"{row[1]} - ({row[2]})"
            level_data[key] = row[0]

        return level_data

    def get_answers(self, level_id):
        logging.info(f"Fetching level answers from level {level_id}")
        cursor = self._connection.execute(ANSWERS_BY_LEVEL_ID, (level_id,))
        return list(map(lambda row: row[0], cursor.fetchall()))

    def get_level_data(self, level_id):
        logging.info(f"Fetching level information from level {level_id}")
        cursor = self._connection.execute(LEVEL_BY_LEVEL_ID, (level_id, ))

        record = cursor.fetchone()

        return {
            "level_info": {
                "level_id": record[0],
                "level_letters": record[1]
            },
            "stage_info": {
                "stage_id": record[2],
                "stage_country": record[3],
                "stage_landmark": record[4]
            }
        }
