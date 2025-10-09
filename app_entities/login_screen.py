from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty

from modules.handle_user_actions.get_user_by_email import get_user_by_email

class LoginScreen(Screen):
    mensaje = StringProperty("")

    def login(self):
        email = self.ids.email.text
        password = self.ids.password.text

        if not email or not password:
            self.mensaje = "❌ ¡Guau! Completa todos los campos 🐕"
            return

        try:
            user = get_user_by_email(email)
            if user and user.password == password:
                self.mensaje = "✅ ¡Guau! Login exitoso 🦴"
                self.ids.email.text = ""
                self.ids.password.text = ""
                self.manager.current = "menu"
            else:
                self.mensaje = "❌ ¡Ups! Email o contraseña incorrectos 🐶"
        except Exception as e:
            self.mensaje = f"❌ ¡Ups! Algo salió mal: {e} 🐕"
