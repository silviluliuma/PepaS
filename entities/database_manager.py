import logging
import psycopg2

from constants.db_config import DB_CONFIG

logger = logging.getLogger(__name__)

class DatabaseManager:
    
    def __init__(self):
        self.config = DB_CONFIG
    
    def get_connection(self):
        try:
            connection = psycopg2.connect(
                host=self.config["host"],
                port=self.config["port"],
                user=self.config["user"],
                password=self.config["password"],
                database=self.config["database"]
            )
            return connection
        except psycopg2.Error as e:
            logger.error(f"There was an error connecting to the database: {e}")
            return None
    
    def test_connection(self):
        conn = self.get_connection()
        if conn:
            logger.info("Connection to PostgreSQL successful")
            conn.close()
            return True
        else:
            logger.error("Error connecting to PostgreSQL")
            return False