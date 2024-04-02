""" Class to manage database connections. """
import logging
import sqlite3

from lib.wow_constants import DATABASE_FILE


class ConnectionManager:
    """ Connection Manager class to manage database connections """
    _connection = None

    def __init__(self):
        """ Creates a connection to the database """
        logging.info("Creating a database connection")
        self._connect()

    def _connect(self):
        """ Connects to the database """
        logging.info(f"Connecting to {DATABASE_FILE}")
        self._connection = sqlite3.connect(DATABASE_FILE, timeout=10)

    def get_connection(self):
        """ Returns the connection """
        logging.info("Getting a connection")
        return self._connection

    def reconnect(self):
        """ Reconnects to the database """
        logging.info("Reconnecting")
        self._connect()
