import hashlib

from constants.new_user_constants import PASSWORD_DOES_NOT_MATCH_MESSAGE, PASSWORD_TOO_SHORT_MESSAGE


def handle_password_hash(self, password:str, confirm_password:str) -> str | None:

        if password != confirm_password:
            self.message = PASSWORD_DOES_NOT_MATCH_MESSAGE
            return None
        if len(password) < 6:
            self.message = PASSWORD_TOO_SHORT_MESSAGE
            return None
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        return password_hash