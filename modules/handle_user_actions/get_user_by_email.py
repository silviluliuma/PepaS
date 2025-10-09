import logging

from database_entities.user import User
from modules.init_database import get_db_connection

logger = logging.getLogger(__name__)

def get_user_by_email(email: str) -> User | None:
        conn = get_db_connection()
        if not conn:
            logger.error("There was an error getting the connection to the database")
            return None

        try:
            with conn.cursor() as cursor:
                cursor.execute("""
                    SELECT id, user_name, user_email, user_phone, user_password_hash, created_at
                    FROM users
                    WHERE user_email = %s
                """, (email,))
                
                result = cursor.fetchone()
                if result:
                    return User(
                        id=result[0],
                        name=result[1],
                        email=result[2],
                        phone=result[3],
                        password_hash=result[4],
                        created_at=result[5]
                    )
                return None
                
        except Exception as e:
            logger.error(f"There was an error getting the user by email: {e}")
            return None
        finally:
            conn.close()
