import logging

from entities.transaction import Transaction

logger = logging.getLogger(__name__)

def update_transaction(self, transaction: Transaction) -> bool:

    if not transaction.id:
        logger.error("Transaction ID is required for update")
        return False

    conn = self.db_manager.get_connection()
    if not conn:
        logger.error("There was an error getting the connection to the database")
        return False

    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                UPDATE transactions 
                SET user_id = %s, type = %s, amount = %s, 
                    category_id = %s, created_at = %s, description = %s
                WHERE id = %s
            """, (
                transaction.user_id,
                transaction.type,
                transaction.amount,
                transaction.category_id,
                transaction.created_at,
                transaction.description,
                transaction.id
            ))
            
            rows_affected = cursor.rowcount
            conn.commit()
            
            if rows_affected > 0:
                logger.info(f"Transaction {transaction.id} updated successfully")
                return True
            else:
                logger.warning(f"No transaction found with ID {transaction.id}")
                return False
            
    except Exception as e:
        logger.error(f"There was an error updating the transaction: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()
