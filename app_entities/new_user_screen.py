from datetime import datetime
import hashlib

from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen

from database_entities.user import User
from modules.handle_user_actions.create_user import create_user

class NewUserScreen(Screen):
    mensaje = StringProperty("")

    def create_account(self):
        name = self.ids.name.text
        email = self.ids.email.text
        phone = self.ids.phone.text
        password = self.ids.password.text
        confirm_password = self.ids.confirm_password.text

        if not name or not email or not password or not confirm_password or not phone:
            self.mensaje = "¡Guau! Completa todos los campos"
            return

        if password != confirm_password:
            self.mensaje = "¡Ups! Las contraseñas no coinciden"
            return

        if len(password) < 6:
            self.mensaje = "¡Guau! La contraseña debe tener al menos 6 caracteres"
            return
        
        password_hash = hashlib.sha256(password.encode()).hexdigest()

        try:
            new_user= User(
                name=name,
                email=email,
                phone=phone,
                password_hash=password_hash
            )
            print(new_user)
            create_user(new_user)
            self.mensaje = "¡Guau! Cuenta creada exitosamente"
            self.ids.name.text = ""
            self.ids.email.text = ""
            self.ids.phone.text = ""
            self.ids.password.text = ""
            self.ids.confirm_password.text = ""
            self.manager.current = "login"
        except Exception as e:
            self.mensaje = f"¡Ups! Algo salió mal: {e}" #CAMBIAR A LOGGING para que no le llegue al user
