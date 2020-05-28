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
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock, mainthread

import kivy.garden.contextmenu
# https://stackoverflow.com/questions/55133377/pycharm-error-kivy-garden-knob-import-successfully-but-not-active-on-script
# https://kivy.org/doc/stable/api-kivy.garden.html

from kivy import Config

Config.set('graphics', 'multisamples', '0')

projects = ['Proj_1', 'proj-2', '3-jorp', '4_jorp']


class ListButton(Button):
    list_btn = ObjectProperty(None)


class MainManager(ScreenManager):
    main_mng = ObjectProperty()


class SubManager(ScreenManager):
    sub_mng = ObjectProperty(None)


class ProjButton(ListButton):
    main_mng = MainManager.main_mng


class MainScreen(Screen):
    cont_proj_list = ObjectProperty(None)
    # main_mng = ObjectProperty()

    def on_release(self, *args):
        """
        https://stackoverflow.com/questions/45934429/bind-a-function-to-multiple-dynamically-created-buttons-in-kivy
        https://stackoverflow.com/questions/46393737/calling-a-method-from-on-release-event-of-a-button-in-a-pop-up
        https://stackoverflow.com/questions/49265887/use-on-press-event-to-change-screen-without-kv-language-for-dynamically-created
        """
        super(ProjButton, self).on_release(*args)
        self.main_mng.current = "proj_scrn"

    @mainthread
    def on_enter(self):
        for idx, name in enumerate(projects):
            button = ProjButton(text=name)
            print(name)
            self.ids.cont_proj_list.add_widget(button)


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
    pass
    # cont_proj_list = ObjectProperty(None)


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
