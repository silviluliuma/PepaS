import logging

from constants.new_user_constants import SUCCESS_CREATE_ACCOUNT_MESSAGE
from database_entities.user import User
from modules.handle_user_actions.create_user import create_user

logger = logging.getLogger(__name__)

def handle_create_new_user(self, name:str, email:str, phone:str, password_hash:str):

    new_user= User(
        name=name,
        email=email,
        phone=phone,
        password_hash=password_hash
    )

    logger.info(f"Creating new user: {new_user}")
    create_user(new_user)
    self.message = SUCCESS_CREATE_ACCOUNT_MESSAGE
    self.ids.name.text = ""
    self.ids.email.text = ""
    self.ids.phone.text = ""
    self.ids.password.text = ""
    self.ids.confirm_password.text = ""
    self.manager.current = "login"
