import logging
from entities.user import User

logger = logging.getLogger(__name__)

def create_user(self, user: User) -> int | None:
        conn = self.db_manager.get_connection()
        if not conn:
            logger.error("There was an error getting the connection to the database")
            return None

        try:
            with conn.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO users (user_name, user_email, user_phone, created_at)
                    VALUES (%s, %s, %s, %s)
                    RETURNING id
                """, (
                    user.name,
                    user.email,
                    user.phone,
                    user.created_at,
                ))
                
                user_id = cursor.fetchone()[0]
                conn.commit()
                logger.info(f"User created with ID: {user_id}")
                return user_id
                
        except Exception as e:
            logger.error(f"There was an error creating the user: {e}")
            conn.rollback()
            return None
        finally:
            conn.close()
    