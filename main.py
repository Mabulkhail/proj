from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

welc = """
MDScreen:
    name: 'welcome'
    MDFloatLayout:
        md_bg_color: 1, 1, 1, 1
        
        MDLabel:
            text: "Indoor Navigation for Faculty Member floor"
            font_size: "26sp"
            pos_hint: {"center_x": 0.54, "center_y": .85}
            color: rgba(0, 0, 59, 255)

        MagicButton:
            text: "Go as guest"
            pos_hint: {"center_x": .5, "center_y": .14}
            on_press:
                self.grow()
                root.manager.current = "main"
                root.manager.transition.direction = "left"
<MagicButton@MagicBehavior+Button>:
    text:root.text
    size_hint: .5, .065
    pos_hint: root.pos_hint
    background_color: 0, 0, 0, 0
    on_press:
        root.on_press
    canvas.before:
        Color:
            rgb: rgba(52, 0, 231, 255)
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [5]
"""

minp = """
class MainApp(MDApp):

    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("welcome_page.kv"))
        screen_manager.add_widget(Builder.load_file("main.kv"))
        return screen_manager

if __name__ == "__main__":
    MainApp().run()
