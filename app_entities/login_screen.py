import hashlib

from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen

from modules.handle_user_actions.get_user_by_email import get_user_by_email

class LoginScreen(Screen):
    mensaje = StringProperty("")

    def login(self):
        email = self.ids.email.text
        password = self.ids.password.text

        if not email or not password:
            self.mensaje = "¡Guau! Completa todos los campos"
            return

        try:
            user = get_user_by_email(email)
            if user:
                # Hash la contraseña ingresada para compararla con la almacenada
                login_password_hash = hashlib.sha256(password.encode()).hexdigest()
                if user.password_hash == login_password_hash:
                    # Guardar el usuario en la sesión
                    App.get_running_app().set_current_user(user)
                    self.mensaje = "¡Guau! Login exitoso"
                    self.ids.email.text = ""
                    self.ids.password.text = ""
                    self.manager.current = "menu"
                else:
                    self.mensaje = "¡Ups! Email o contraseña incorrectos"
            else:
                self.mensaje = "¡Ups! Email o contraseña incorrectos"
        except Exception as e:
            self.mensaje = f"¡Ups! Algo salió mal: {e}" #CAMBIAR A LOGGING para que no le llegue al user
