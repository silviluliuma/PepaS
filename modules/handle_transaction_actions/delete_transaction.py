import logging

from modules.init_database import get_db_connection

logger = logging.getLogger(__name__)

def delete_transaction(transaction_id: int) -> bool:
    conn = get_db_connection()
    if not conn:
        logger.error("There was an error getting the connection to the database")
        return False

    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                DELETE FROM transactions 
                WHERE id = %s
            """, (transaction_id,))
            
            rows_affected = cursor.rowcount
            conn.commit()
            
            if rows_affected > 0:
                logger.info(f"Transaction {transaction_id} deleted successfully")
                return True
            else:
                logger.warning(f"No transaction found with ID {transaction_id}")
                return False
            
    except Exception as e:
        logger.error(f"There was an error deleting the transaction: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()
