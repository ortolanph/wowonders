import logging

from lib.wow_controller import WOWController

logging.basicConfig(
    format='%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d :: %(message)s',
    level=logging.INFO)

if __name__ == '__main__':
    logging.info("Starting the main code")
    controller = WOWController()

    controller.retrieve_data()
