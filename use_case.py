import logging

from entities.transaction import Transaction
from entities.transaction_manager import TransactionManager
from entities.user import User
from modules.init_database import init_database

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("Hello PepaS! Starting the application...")
    
    # We test the connection to the database
    conn = init_database()
    
    # We create a user to insert in database
    user = User(
        id=None,
        name="Silvia",
        email="silvia@example.com",
        phone="+3434567890",
        created_at=None
    )
    
    logger.info(f"User created: {user}")
    
    # We create the user in the database
    user_id = create_user(user)
    
    if not user_id:
        logger.error("😞 No se pudo crear el usuario")
        exit(1)
    
    logger.info(f"🎉 ¡Usuario creado exitosamente con ID {user_id}!")
    
    # Ahora creemos una transacción para este usuario
    transaccion = Transaction(
        id=None,
        user_id=user_id,
        type="expense",
        amount=50.0,
        category_id=1,
        description="Almuerzo en restaurante",
        created_at=None
    )
    
    logger.info(f"Transacción creada: {transaccion}")
    
    # Probemos guardar en la base de datos
    transaction_manager = TransactionManager()
    transaction_id = transaction_manager.create_transaction(transaccion)
    
    if transaction_id:
        logger.info(f"🎉 ¡Transacción guardada exitosamente con ID {transaction_id}!")
        
        # Probemos las operaciones READ
        logger.info("\n--- Probando operaciones READ ---")
        
        # Obtener transacción por ID
        transaccion_obtenida = transaction_manager.get_transaction_by_id(transaction_id)
        if transaccion_obtenida:
            logger.info(f"✅ Transacción encontrada: {transaccion_obtenida.description} - ${transaccion_obtenida.amount}")
        else:
            logger.error("❌ No se pudo obtener la transacción")
        
        # Obtener transacciones del usuario
        transacciones_usuario = transaction_manager.get_transactions_by_user(user_id, limit=5)
        logger.info(f"✅ Transacciones del usuario: {len(transacciones_usuario)} encontradas")
        for t in transacciones_usuario:
            print(f"  - {t.type}: ${t.amount} - {t.description}")
        
        # Probemos las operaciones UPDATE y DELETE
        logger.info("\n--- Probando operaciones UPDATE y DELETE ---")
        
        # Actualizar la transacción
        transaccion_obtenida.amount = 75.0
        transaccion_obtenida.description = "Almuerzo en restaurante (actualizado)"
        
        if transaction_manager.update_transaction(transaccion_obtenida):
            logger.info("✅ Transacción actualizada exitosamente")
        else:
            logger.error("❌ Error actualizando la transacción")
        
        # Verificar la actualización
        transaccion_actualizada = transaction_manager.get_transaction_by_id(transaction_id)
        if transaccion_actualizada:
            logger.info(f"✅ Transacción actualizada: ${transaccion_actualizada.amount} - {transaccion_actualizada.description}")
        
        # Eliminar la transacción (opcional - comentado para no perder datos)
        # if transaction_manager.delete_transaction(transaction_id):
        #     logger.info("✅ Transacción eliminada exitosamente")
        # else:
        #     print("❌ Error eliminando la transacción")
            
    else:
        print("😞 No se pudo guardar la transacción")
