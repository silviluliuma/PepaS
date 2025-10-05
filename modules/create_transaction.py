import logging

from entities.transaction import Transaction

logger = logging.getLogger(__name__)

def create_transaction(self, transaction: Transaction) -> int | None:

    conn = self.db_manager.get_connection()
    if not conn:
        logger.error("There was an error getting the connection to the database")
        return None

    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO transactions (user_id, type, amount, category_id, description, created_at)
                VALUES (%s, %s, %s, %s, %s, %s)
                RETURNING id
            """, (
                transaction.user_id,
                transaction.type,
                transaction.amount,
                transaction.category_id,
                transaction.description,
                transaction.created_at
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
