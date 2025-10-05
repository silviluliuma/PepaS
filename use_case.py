from entities.database_manager import DatabaseManager
from entities.transaction import Transaction
from entities.transaction_manager import TransactionManager

if __name__ == "__main__":
    print("¡Hola PepaS! Empezando a construir la aplicación...")
    
    # Probemos la conexión a la base de datos
    db_manager = DatabaseManager()
    db_manager.test_connection()
    
    # Probemos crear una transacción
    transaccion = Transaction(
        id=None,
        user_id=1,
        type="gasto",
        amount=50.0,
        category_id=1,
        description="Almuerzo en restaurante",
        created_at=None
    )
    
    print(f"Transacción creada: {transaccion}")
    
    # Probemos guardar en la base de datos
    transaction_manager = TransactionManager()
    transaction_id = transaction_manager.create_transaction(transaccion)
    
    if transaction_id:
        print(f"🎉 ¡Transacción guardada exitosamente con ID {transaction_id}!")
        
        # Probemos las operaciones READ
        print("\n--- Probando operaciones READ ---")
        
        # Obtener transacción por ID
        transaccion_obtenida = transaction_manager.get_transaction_by_id(transaction_id)
        if transaccion_obtenida:
            print(f"✅ Transacción encontrada: {transaccion_obtenida.description} - ${transaccion_obtenida.amount}")
        else:
            print("❌ No se pudo obtener la transacción")
        
        # Obtener transacciones del usuario
        transacciones_usuario = transaction_manager.get_transactions_by_user(1, limit=5)
        print(f"✅ Transacciones del usuario: {len(transacciones_usuario)} encontradas")
        for t in transacciones_usuario:
            print(f"  - {t.type}: ${t.amount} - {t.description}")
        
        # Probemos las operaciones UPDATE y DELETE
        print("\n--- Probando operaciones UPDATE y DELETE ---")
        
        # Actualizar la transacción
        transaccion_obtenida.amount = 75.0
        transaccion_obtenida.description = "Almuerzo en restaurante (actualizado)"
        
        if transaction_manager.update_transaction(transaccion_obtenida):
            print("✅ Transacción actualizada exitosamente")
        else:
            print("❌ Error actualizando la transacción")
        
        # Verificar la actualización
        transaccion_actualizada = transaction_manager.get_transaction_by_id(transaction_id)
        if transaccion_actualizada:
            print(f"✅ Transacción actualizada: ${transaccion_actualizada.amount} - {transaccion_actualizada.description}")
        
        # Eliminar la transacción (opcional - comentado para no perder datos)
        # if transaction_manager.delete_transaction(transaction_id):
        #     print("✅ Transacción eliminada exitosamente")
        # else:
        #     print("❌ Error eliminando la transacción")
            
    else:
        print("😞 No se pudo guardar la transacción")
