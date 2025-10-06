import logging

from entities.transaction import Transaction

logger = logging.getLogger(__name__)

def get_transactions_by_user(self, user_id: int, limit: int = 10) -> list[Transaction]:

    conn = self.db_manager.get_connection()
    if not conn:
        return []
    
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT id, user_id, type, amount, category_id, created_at, description
                FROM transactions 
                WHERE user_id = %s
                ORDER BY created_at DESC
                LIMIT %s
            """, (user_id, limit))
            
            transactions = []
            for row in cursor.fetchall():
                transaction = Transaction(
                    id=row[0],
                    user_id=row[1],
                    type=row[2],
                    amount=row[3],
                    category_id=row[4],
                    created_at=row[5],
                    description=row[6],
                )
                transactions.append(transaction)
            
            return transactions
            
    except Exception as e:
        logger.error(f"There was an error getting the transactions for the user: {e}")
        return []
    finally:
        conn.close()

