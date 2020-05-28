from kivy.app import App
# kivy.require("1.10.0")
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.uix.widget import Widget
#from kivy.base import runTouchApp
from kivy.properties import StringProperty, ObjectProperty, NumericProperty
from functools import partial


class ScrollableLabelDataEntryInstructions(BoxLayout):
    pass


class NewGarageScreen(Screen):
    pass


class ContinueEditingScreen(Screen):
    pass


class GarageNameBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(GarageNameBoxLayout, self).__init__(**kwargs)
        self.orientation = "vertical"
        Clock.schedule_interval(self.create_button, 5)

    def create_button(self, *args):
        self.box_share2.clear_widgets()
        app = App.get_running_app()
        sm = app.root

        #put GarageNameStartList data into app class, then pull from it in this class
        top_button_share = 1.1
        color = (.4, .4, .4, 1)
        for text in app.GarageNameStartList:
            top_button_share -= .4
            id_ = text
            button_share = Button(background_normal='',
                                  background_color = color,
                                  id = id_,
                                  pos_hint = {"x": 0, "top": top_button_share},
                                  size_hint_y = None,
                                  height = 60,
                                  font_size = 30,
                                  text = text)
            button_share.bind(on_press=lambda *args: setattr(sm, 'current', "main"))
            self.box_share2.add_widget(button_share)

    def changer(self, *args):
        ScreenManager()
        #app = App.get_running_app()
        screenmanager.current = 'MainScreen'


class BackHomeWidget(Widget):
    pass


class MainScreen(Screen):
    pass


class AnotherScreen(Screen):
    pass


class ScreenManagement(ScreenManager):
    pass


presentation = Builder.load_file("example_on_press.kv")


class MainApp(App):
    GarageNameStartList = ["Test1", "Test2", "Test3"]

    def Update_GarageNameStartList(self, *args):
        self.GarageNameStartList = ["Test1", "Test2", "Test3"]

    def build(self):
        return presentation


if __name__ == "__main__":
    MainApp().run()
