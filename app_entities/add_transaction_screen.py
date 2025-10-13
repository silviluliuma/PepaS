from datetime import datetime
import logging

from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen

from constants.new_transaction_constants import TRANSACTION_TYPE_MAP
from database_entities.transaction import Transaction
from modules.handle_transaction_actions.create_transaction import create_transaction

logger = logging.getLogger(__name__)

class AddTransactionScreen(Screen):
    message = StringProperty("")

    def guardar_transaccion(self):
        type_text = self.ids.type.text
        amount = self.ids.amount.text
        description = self.ids.description.text

        transaction_type = TRANSACTION_TYPE_MAP.get(type_text, 0)

        try:
            # Obtener el usuario actual de la sesión
            current_user_id = App.get_running_app().get_current_user_id()
            if not current_user_id:
                self.message = "¡Guau! Debes iniciar sesión primero"
                return
            # Crear transacción
            amount = float(amount)
            transaction = Transaction(
                id=None,
                user_id=current_user_id,
                type=transaction_type,
                amount=amount,
                category_id=None,
                description=description,
                created_at=datetime.now()
            )
            create_transaction(transaction)
            self.message = "¡Guau! Transacción guardada con éxito"
            self.ids.amount.text = ""
            self.ids.description.text = ""
            self.ids.type.text = "Gasto"
        except ValueError:
            self.message = "¡Guau guau! El amount debe ser un número válido"
        except Exception as e:
            self.message = f"¡Ups! Algo salió mal: {e}"