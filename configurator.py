from time import time
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import NumericProperty, StringProperty, BooleanProperty,\
    ListProperty
from kivy.animation import Animation
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button

# kv_str = Builder.load_string('''
# <ColourScreen>:
#     BoxLayout:
#         Button:
#             text: "My button"
#
# BoxLayout:
#     orientation: "vertical"
#     ActionBar:
#         pos_hint: {'top':1}
#         ActionView:
#             use_separator: True
#             ActionPrevious:
#                 title: 'Car Configurator'
#                 with_previous: False
#                 app_icon: "logo.png"
#             ActionButton:
#                 text: '1 - Colour'
#             ActionButton:
#                 text: '2 - Engine'
#             ActionButton:
#                 text: '3 - Equimpment'
#             ActionButton:
#                 text: '4 - Loan'
#             ActionButton:
#                 text: 'Exit'
#     ScreenManager:
#         id: sm
#
# ''')

class ColourScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(ColourScreen(name="colour"))

class CarConfigurator(App):
    def build(self):
        self.title = "Car Configurator"
        self.icon = "logo.png"



if __name__ == '__main__':
    CarConfigurator().run()