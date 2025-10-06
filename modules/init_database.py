import logging
from constants.db_config import DB_CONFIG

logger = logging.getLogger(__name__)

def init_database(self):
    self.config = DB_CONFIG
    conn = self.get_connection()
    if not conn:
        logger.error("There was an error getting the connection to the database")
        return False
    return conn