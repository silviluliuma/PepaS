from datetime import datetime

from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen

from database_entities.transaction import Transaction
from modules.handle_transaction_actions.create_transaction import create_transaction

class AddTransactionScreen(Screen):
    mensaje = StringProperty("")

    def guardar_transaccion(self):
        tipo_text = self.ids.tipo.text
        monto = self.ids.monto.text
        descripcion = self.ids.descripcion.text

        # Convertir texto español a inglés para la base de datos TO DO: hacer bien el mapeo
        tipo_map = {
            "Gasto": "expense",
            "Ingreso": "income"
        }
        tipo = tipo_map.get(tipo_text, "expense")

        try:
            # Obtener el usuario actual de la sesión
            current_user_id = App.get_running_app().get_current_user_id()
            if not current_user_id:
                self.mensaje = "¡Guau! Debes iniciar sesión primero"
                return
            
            monto = float(monto)
            transaction = Transaction(
                id=None,
                user_id=current_user_id,
                type=tipo,
                amount=monto,
                category_id=None,
                description=descripcion,
                created_at=datetime.now()
            )
            create_transaction(transaction)
            self.mensaje = "¡Guau! Transacción guardada con éxito"
            self.ids.monto.text = ""
            self.ids.descripcion.text = ""
            self.ids.tipo.text = "Gasto"
        except ValueError:
            self.mensaje = "¡Guau guau! El monto debe ser un número válido"
        except Exception as e:
            self.mensaje = f"¡Ups! Algo salió mal: {e}"