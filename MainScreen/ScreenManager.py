"""
https://stackoverflow.com/questions/41337143/switch-screenmanager-inside-layout
Ideas:
https://www.python-forum.de/viewtopic.php?f=4&t=46427
"""
from kivy import Config
win_px = 960
Config.set('graphics', 'width', str(win_px))
Config.set('graphics', 'height', str(int(win_px*0.618)))
Config.set('graphics', 'minimum_width', str(int(win_px*0.6)))
Config.set('graphics', 'minimum_height', str(int(win_px*0.618*.5)))

import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock

import kivy.garden.contextmenu
# https://stackoverflow.com/questions/55133377/pycharm-error-kivy-garden-knob-import-successfully-but-not-active-on-script
# https://kivy.org/doc/stable/api-kivy.garden.html

from kivy import Config
Config.set('graphics', 'multisamples', '0')


class ListButton(Button):
    list_btn = ObjectProperty(None)


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
    head = ObjectProperty(None)


class Footer(BoxLayout):
    pass


class ProjectGridLayout(GridLayout):
    cont_proj_list = ObjectProperty(None)


class SampleGridLayout(GridLayout):
    cont_samp_list = ObjectProperty(None)


class MainMenu(FloatLayout):
    main_menu = ObjectProperty(None)

    def close_menu(self):
        self.ids['main_menu'].close_all()


class ClassAllScreen(BoxLayout):
    main_win = ObjectProperty(None)


class ClassAllScreenApp(App):

    def build(self):
        self.root = ClassAllScreen()
        return self.root


if __name__ == '__main__':
    ClassAllScreenApp().run()
