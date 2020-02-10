"""
https://stackoverflow.com/questions/41337143/switch-screenmanager-inside-layout
Ideas:
https://www.python-forum.de/viewtopic.php?f=4&t=46427
"""
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.clock import Clock

from kivy import Config
Config.set('graphics', 'multisamples', '0')


class MainManager(ScreenManager):
    main_mng = ObjectProperty(None)


class SubManager(ScreenManager):
    sub_mng = ObjectProperty(None)


class MainScreen(Screen):
    pass


class ProjectScreen(Screen):
    pass


class OverviewScreen(Screen):
    pass


class SampleScreen(Screen):
    pass


class Header(BoxLayout):
    pass


class Footer(BoxLayout):
    pass


class ClassAllScreen(BoxLayout):
    main_win = ObjectProperty(None)


class ClassAllScreenApp(App):

    def build(self):
        self.root = ClassAllScreen()
        return self.root


if __name__ == '__main__':
    ClassAllScreenApp().run()
