from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager


class MainApp(MDApp):

    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("welcome_page.kv"))
        screen_manager.add_widget(Builder.load_file("main.kv"))
        return screen_manager

if __name__ == "__main__":
    MainApp().run()
