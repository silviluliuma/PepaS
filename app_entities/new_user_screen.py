import logging

from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen

from constants.new_user_constants import MANDATORY_FIELDS, MISSING_FIELDS_MESSAGE, ERROR_MESSAGE
from modules.handle_user_actions.handle_password_hash import handle_password_hash
from modules.handle_user_actions.handle_create_new_user import handle_create_new_user

logger = logging.getLogger(__name__)

class NewUserScreen(Screen):
    message = StringProperty("")

    def create_account(self):

        name = self.ids.name.text
        email = self.ids.email.text
        phone = self.ids.phone.text
        password = self.ids.password.text
        confirm_password = self.ids.confirm_password.text

        if not all(field.strip() for field in MANDATORY_FIELDS):
            self.message = MISSING_FIELDS_MESSAGE
            return

        password_hash = handle_password_hash(self, password, confirm_password)

        if password_hash is None:
            return
    
        try:
            handle_create_new_user(self, name, email, phone, password_hash)
        except Exception as e:
            self.message = ERROR_MESSAGE
            logger.error(f"Error trying to create account: {e}")
