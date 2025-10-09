import os

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder

from app_entities.login_screen import LoginScreen
from app_entities.new_user_screen import NewUserScreen
from app_entities.menu_screen import MenuScreen
from app_entities.add_transaction_screen import AddTransactionScreen

class PepaApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_user = None  # Almacenar el usuario logueado
    
    def set_current_user(self, user):
        """Establecer el usuario actual"""
        self.current_user = user
    
    def get_current_user_id(self):
        """Obtener el ID del usuario actual"""
        return self.current_user.id if self.current_user else None
    
    def build(self):
        kv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'pepa.kv')
        Builder.load_file(kv_path)
        
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(NewUserScreen(name="new_user"))
        sm.add_widget(MenuScreen(name="menu"))
        sm.add_widget(AddTransactionScreen(name="add_transaction"))
        sm.current = "login"
        return sm