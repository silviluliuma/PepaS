from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty

from database_entities.transaction import Transaction
from modules.handle_transaction_actions.create_transaction import create_transaction

class AddTransactionScreen(Screen):
    mensaje = StringProperty("")

    def guardar_transaccion(self):
        tipo_text = self.ids.tipo.text
        monto = self.ids.monto.text
        descripcion = self.ids.descripcion.text

        # Convertir texto español a inglés para la base de datos
        tipo_map = {
            "Gasto": "expense",
            "Ingreso": "income"
        }
        tipo = tipo_map.get(tipo_text, "expense")

        try:
            monto = float(monto)
            transaction = Transaction(
                id=None,
                user_id=1,
                type=tipo,
                amount=monto,
                category_id=None,
                description=descripcion,
                created_at=None
            )
            self.mensaje = f"✅ ¡Guau! Transacción guardada con éxito 🦴"
            self.ids.monto.text = ""
            self.ids.descripcion.text = ""
            self.ids.tipo.text = "Gasto"
        except ValueError:
            self.mensaje = "❌ ¡Guau guau! El monto debe ser un número válido 🐕"
        except Exception as e:
            self.mensaje = f"❌ ¡Ups! Algo salió mal: {e} 🐶"