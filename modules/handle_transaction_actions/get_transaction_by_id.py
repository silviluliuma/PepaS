import logging

from entities.transaction import Transaction

logger = logging.getLogger(__name__)

def get_transaction_by_id(self, transaction_id: int) -> Transaction | None:

    conn = self.db_manager.get_connection()
    if not conn:
        return None
    
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT id, user_id, type, amount, category_id, created_at, description
                FROM transactions 
                WHERE id = %s
            """, (transaction_id,))
            
            row = cursor.fetchone()
            if row:
                return Transaction(
                    id=row[0],
                    user_id=row[1],
                    type=row[2],
                    amount=row[3],
                    category_id=row[4],
                    created_at=row[5],
                    description=row[6]
                )
            return None
            
    except Exception as e:
        logger.error(f"There was an error getting the transaction: {e}")
        return None
    finally:
        conn.close()