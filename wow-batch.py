import logging

from lib.service.wow_service import WOWService

logging.basicConfig(
    format='%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d :: %(message)s',
    level=logging.INFO)

if __name__ == '__main__':
    logging.info("Starting the main code")
    controller = WOWService()

    controller.retrieve_data()
