from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image

from kivy.cache import Cache






class Manager(ScreenManager):


    def __init__(self, *args, **kwargs):
        image = Image(source="red.png", allow_stretch=True)
        super(Manager, self).__init__(*args, **kwargs)
        # define screens
        # colour screen

        colour_screen = Screen(name = "1 - Colour")
        colour_layout = BoxLayout(spacing = 1, orientation="vertical")
        colour_layout.add_widget(Label(valign="top", text="Choose Colour", size_hint=(1,0.5)))
        car_image_layout = GridLayout(cols = 1, rows = 1)
        car_image_layout.add_widget(image)
        colour_layout.add_widget(car_image_layout)

        def changecolor(btn):
            image.source = "{}.png".format(btn.text)
            image.reload()
        switches = GridLayout(cols=4, size_hint=(1, 0.2))
        switches.add_widget(Button(text="Red", on_release=changecolor))
        switches.add_widget(Button(text="Blue", on_release=changecolor))
        switches.add_widget(Button(text="Silver", on_release=changecolor))
        switches.add_widget(Button(text="Orange", on_release=changecolor))

        colour_layout.add_widget(switches)
        colour_screen.add_widget(colour_layout)
        self.add_widget(colour_screen)

        # engine screen
        engine_screen = Screen(name = "2 - Engine")
        self.add_widget(engine_screen)

        # equipment screen
        equipment_screen = Screen(name = "3 - Equipment")
        self.add_widget(equipment_screen)

        # loan screen
        loan_screen = Screen(name = "4 - Loan")
        self.add_widget(loan_screen)
    def callback(self, value):
        self.image(source="green.png")



class Nav(GridLayout):

    def __init__(self, sm=None, *args, **kwargs):
        super(Nav, self).__init__(*args, **kwargs)
        self.sm = sm
        self.rows = 1
        self.cols = 5
        self.row_force_default = True
        self.row_default_height = 40
        self.size_hint = (1, .1)
        self.add_widget(Button(text="1 - Colour", on_release=self.change))
        self.add_widget(Button(text="2 - Engine", on_release=self.change))
        self.add_widget(Button(text="3 - Equipment", on_release=self.change))
        self.add_widget(Button(text="4 - Loan", on_release=self.change))
        self.add_widget(Button(text="Exit", on_release=App.stop, size_hint = (.4,1),
                               background_color = [.4,.4,.4,1]))

    def change(self, btn):
        self.sm.current = btn.text


class Root(BoxLayout):

    def __init__(self, *args, **kwargs):
        super(Root, self).__init__(*args, **kwargs)
        self.orientation = "vertical"
        sm = Manager()

        self.add_widget(Nav(sm=sm))
        self.add_widget(sm)


class TestApp(App):


    def build(App):
        App.title = "Car configurator"
        App.icon = "logo.png"
        return Root()




if __name__ == '__main__':
    TestApp().run()

