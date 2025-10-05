from entities.database_manager import DatabaseManager
from entities.transaction import Transaction
from modules.create_transaction import create_transaction
from modules.get_transaction_by_id import get_transaction_by_id
from modules.get_user_transactions import get_transactions_by_user
from modules.update_transaction import update_transaction
from modules.delete_transaction import delete_transaction


class TransactionManager:
    
    def __init__(self):
        self.db_manager = DatabaseManager()
    
    def create_transaction(self, transaction: Transaction) -> int | None:
        return create_transaction(self, transaction)
    
    def get_transaction_by_id(self, transaction_id: int) -> Transaction | None:
        return get_transaction_by_id(self, transaction_id)
    
    def get_transactions_by_user(self, user_id: int, limit: int = 10) -> list[Transaction]:
        return get_transactions_by_user(self, user_id, limit)
    
    def update_transaction(self, transaction: Transaction) -> bool:
        return update_transaction(self, transaction)
    
    def delete_transaction(self, transaction_id: int) -> bool:
        return delete_transaction(self, transaction_id)
