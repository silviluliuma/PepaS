import logging
from datetime import datetime

from entities.transaction import Transaction
from entities.user import User
from modules.handle_transaction_actions.create_transaction import create_transaction
from modules.handle_transaction_actions.delete_transaction import delete_transaction
from modules.handle_transaction_actions.get_transaction_by_id import get_transaction_by_id
from modules.handle_transaction_actions.get_transactions_by_user import get_transactions_by_user
from modules.handle_transaction_actions.update_transaction import update_transaction
from modules.handle_user_actions.create_user import create_user
from modules.handle_user_actions.get_user_by_email import get_user_by_email
from modules.init_database import init_database

# Configure logging to show in the terminal
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("Hello PepaS! Starting the application...")
    
    # We test the connection to the database
    if not init_database():
        logger.error("Failed to connect to database")
        exit(1)
    
    # We create a user to insert in database
    user = User(
        id=None,
        name="Silvia",
        email="silvia@example.com",
        phone="+3434567890",
        created_at=datetime.now()
    )
    
    logger.info(f"User created: {user}")
    
    # Check if user already exists
    existing_user = get_user_by_email(user.email)
    if existing_user:
        logger.info(f"User already exists with ID {existing_user.id}")
        user_id = existing_user.id
    else:
        # We create the user in the database
        user_id = create_user(user)
        
        if not user_id:
            logger.error("We couldn't create the user")
            exit(1)
        
        logger.info(f"🎉 User created successfully with ID {user_id}!")
    
    # Now we create a transaction for this user
    transaction = Transaction(
        id=None,
        user_id=user_id,
        type="expense",
        amount=50.0,
        category_id=None,  # Changed to None since category doesn't exist yet
        description="Almuerzo en restaurante",
        created_at=datetime.now()
    )
    
    logger.info(f"Transaction created: {transaction}")
    
    # We test to save in the database
    transaction_id = create_transaction(transaction)
    
    if transaction_id:
        logger.info(f"🎉 Transaction saved successfully with ID {transaction_id}!")
        
        # We test the READ operations
        logger.info("\n--- Testing READ operations ---")
        
        # We get the transaction by ID
        transaction_obtained = get_transaction_by_id(transaction_id)
        if transaction_obtained:
            logger.info(f"✅ Transaction found: {transaction_obtained.description} - ${transaction_obtained.amount}")
        else:
            logger.error("❌ We couldn't get the transaction")
        
        # We get the transactions of the user
        transactions_user = get_transactions_by_user(user_id, limit=5)
        logger.info(f"✅ Transactions of the user: {len(transactions_user)} found")
        for t in transactions_user:
            logger.info(f"  - {t.type}: ${t.amount} - {t.description}")
        
        # We test the UPDATE and DELETE operations
        logger.info("\n--- Testing UPDATE and DELETE operations ---")
        
        # We update the transaction
        transaction_obtained.amount = 75.0
        transaction_obtained.description = "Almuerzo en restaurante (actualizado)"
        
        if update_transaction(transaction_obtained):
            logger.info("✅ Transaction updated successfully")
        else:
            logger.error("❌ Error updating the transaction")
        
        # We check the update
        transaction_updated = get_transaction_by_id(transaction_id)
        if transaction_updated:
            logger.info(f"✅ Transaction updated: ${transaction_updated.amount} - {transaction_updated.description}")
        
        # We delete the transaction (optional - commented to not lose data)
        # if delete_transaction(transaction_id):
        #     logger.info("✅ Transaction deleted successfully")
        # else:
        #     logger.error("❌ Error deleting the transaction")
            
    else:
        logger.error("😞 We couldn't save the transaction")
