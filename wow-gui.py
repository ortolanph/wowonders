import logging

from lib.ui.wowui import WOWGui

logging.basicConfig(
    format='%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d :: %(message)s',
    level=logging.INFO)

if __name__ == '__main__':
    gui = WOWGui()
    gui.run()
