import hashlib
import logging

from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen

from constants.login_constants import MISSING_FIELDS_MESSAGE, SUCCESS_LOGIN_MESSAGE, INCORRECT_CREDENTIALS_MESSAGE, ERROR_MESSAGE
from modules.handle_user_actions.get_user_by_email import get_user_by_email

logger = logging.getLogger(__name__)

class LoginScreen(Screen):
    message = StringProperty("")

    def login(self):
        email = self.ids.email.text
        password = self.ids.password.text

        if not email or not password:
            self.message = MISSING_FIELDS_MESSAGE
            return

        try:
            user = get_user_by_email(email)
            if user:
                login_password_hash = hashlib.sha256(password.encode()).hexdigest()
                if user.password_hash == login_password_hash:
                    App.get_running_app().set_current_user(user)
                    self.message = SUCCESS_LOGIN_MESSAGE
                    self.ids.email.text = ""
                    self.ids.password.text = ""
                    self.manager.current = "menu"
                else:
                    self.message = INCORRECT_CREDENTIALS_MESSAGE
            else:
                self.message = INCORRECT_CREDENTIALS_MESSAGE
        except Exception as e:
            self.message = ERROR_MESSAGE
            logger.error(f"Error trying to login: {e}")
