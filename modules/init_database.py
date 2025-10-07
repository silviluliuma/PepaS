import logging
import psycopg2

from constants.db_config import DB_CONFIG

logger = logging.getLogger(__name__)

def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=DB_CONFIG["host"],
            port=DB_CONFIG["port"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
            database=DB_CONFIG["database"]
        )
        return conn
    except Exception as e:
        logger.error(f"There was an error connecting to the database: {e}")
        return None

def init_database():
    conn = get_db_connection()
    if conn:
        logger.info("Database connection established successfully")
        conn.close()
        return True
    return False