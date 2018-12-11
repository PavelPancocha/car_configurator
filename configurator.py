from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
from kivy.uix.image import Image

from kivy.cache import Cache


class Manager(ScreenManager):

    def __init__(self, *args, **kwargs):
        image = Image(source="red.png", allow_stretch=True)
        price = 350000
        price_text = "Selected configuration cost: {} Kč".format(price)
        added_price_colour = 0
        added_price_engine = 0
        added_price_equipment = 0
        super(Manager, self).__init__(*args, **kwargs)
        # define screens
        # colour screen

        colour_screen = Screen(name="1 - Colour")
        colour_layout = BoxLayout(spacing=1, orientation="vertical")
        colour_layout.add_widget(Label(valign="top", text="Choose Colour", bold=True, size_hint=(1, 0.2)))
        colour_price_label = Label(halign="right", text=price_text, size_hint=(1, 0.2))
        colour_layout.add_widget(colour_price_label)
        car_image_layout = GridLayout(cols=1, rows=1)
        car_image_layout.add_widget(image)
        colour_layout.add_widget(car_image_layout)

        def changecolor(btn):
            new_image_name = str(btn.text)
            new_image_name = new_image_name.split("\n")
            print(new_image_name)
            image.source = "{}.png".format(new_image_name[0])
            image.reload()
            nonlocal price, added_price_colour
            price -= added_price_colour
            added_price_colour = 0
            if btn.text == "Red\nStandart color":
                added_price_colour = 0
            elif btn.text == "Blue\n+5000 Kč":
                added_price_colour = 5000
            elif btn.text == "Silver\n+10000 Kč":
                added_price_colour = 10000
            elif btn.text == "Orange\n+13000 Kč":
                added_price_colour = 13000
            price += added_price_colour

            nonlocal price_text
            price_text = "Selected configuration cost: {} Kč".format(price)
            colour_price_label.text = price_text
            engine_price_label.text = price_text

        switches = GridLayout(cols=4, size_hint=(1, 0.2))
        switches.add_widget(Button(text="Red\nStandard color", halign="center", on_release=changecolor))
        switches.add_widget(Button(text="Blue\n+5000 Kč", halign="center", on_release=changecolor))
        switches.add_widget(Button(text="Silver\n+10000 Kč", halign="center", on_release=changecolor))
        switches.add_widget(Button(text="Orange\n+13000 Kč", halign="center", on_release=changecolor))

        colour_layout.add_widget(switches)
        colour_screen.add_widget(colour_layout)
        self.add_widget(colour_screen)

        # engine screen
        def changeengine(btn):
            nonlocal price, added_price_engine
            price -= added_price_engine
            added_price_engine = 0
            btn_txt = str(btn.text).split("\n")
            print(btn_txt)
            if btn_txt[0] == "80 kW":
                added_price_engine = 0
            elif btn_txt[0] == "110 kW":

                if btn_txt[1] == "Manual Transmission":
                    added_price_engine = 20000
                else:
                    added_price_engine = 40000
            price += added_price_engine

            nonlocal price_text
            price_text = "Selected configuration cost: {} Kč".format(price)
            colour_price_label.text = price_text
            engine_price_label.text = price_text

        engine_screen = Screen(name="2 - Engine")
        engine_layout = BoxLayout(spacing=1, orientation="vertical")
        engine_layout.add_widget(Label(valign="top", text="Choose Engine", bold=True, size_hint=(1, 0.2)))
        engine_price_label = Label(halign="right", text=price_text, size_hint=(1, 0.2))
        engine_layout.add_widget(engine_price_label)
        engines = GridLayout(cols=3)
        engines.add_widget(ToggleButton(text="80 kW\n"
                                             "Manual Transmission\n"
                                             "0-100 in 12 s.\n\n"
                                             "Standard engine", halign="left", on_release=changeengine,
                                        group="engine", state="down"))
        engines.add_widget(ToggleButton(text="110 kW\n"
                                             "Manual Transmission\n"
                                             "0-100 in 8 s.\n\n"
                                             "+ 20 000 Kč", halign="left", on_release=changeengine, group="engine"))
        engines.add_widget(ToggleButton(text="110 kW\n"
                                             "Automatic Transmission\n"
                                             "0-100 in 7.5 s.\n\n"
                                             "+40 000 Kč", halign="left", on_release=changeengine, group="engine"))
        engine_layout.add_widget(engines)

        engine_screen.add_widget(engine_layout)
        self.add_widget(engine_screen)

        # equipment screen
        equipment_screen = Screen(name="3 - Equipment")
        self.add_widget(equipment_screen)

        # loan screen
        loan_screen = Screen(name="4 - Loan")
        self.add_widget(loan_screen)




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
        self.add_widget(Button(text="Exit", on_release=App.stop, size_hint=(.4, 1),
                               background_color=[.4, .4, .4, 1]))

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
