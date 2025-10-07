from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
import os

from app_entities.menu_screen import MenuScreen
from app_entities.add_transaction_screen import AddTransactionScreen

class PepaApp(App):
    def build(self):
        kv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'pepa.kv')
        Builder.load_file(kv_path)
        
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name="menu"))
        sm.add_widget(AddTransactionScreen(name="add_transaction"))
        sm.current = "menu"
        return sm