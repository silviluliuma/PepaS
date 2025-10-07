import logging

from database_entities.transaction import Transaction
from modules.init_database import get_db_connection

logger = logging.getLogger(__name__)

def create_transaction(transaction: Transaction) -> int | None:
    conn = get_db_connection()
    if not conn:
        logger.error("There was an error getting the connection to the database")
        return None

    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO transactions (user_id, type, amount, category_id, created_at, description)
                VALUES (%s, %s, %s, %s, %s, %s)
                RETURNING id
            """, (
                transaction.user_id,
                transaction.type,
                transaction.amount,
                transaction.category_id,
                transaction.created_at,
                transaction.description,
            ))
            
            transaction_id = cursor.fetchone()[0]
            conn.commit()
            logger.info(f"Transaction created with ID: {transaction_id}")
            return transaction_id
            
    except Exception as e:
        logger.error(f"There was an error creating the transaction: {e}")
        conn.rollback()
        return None
    finally:
        conn.close()
