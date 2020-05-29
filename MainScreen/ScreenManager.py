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
from kivy.uix.screenmanager import ScreenManager, Screen, CardTransition
from kivy.clock import Clock, mainthread
from kivy.uix.popup import Popup

import kivy.garden.contextmenu
# https://stackoverflow.com/questions/55133377/pycharm-error-kivy-garden-knob-import-successfully-but-not-active-on-script
# https://kivy.org/doc/stable/api-kivy.garden.html

from kivy import Config

Config.set('graphics', 'multisamples', '0')

projects = ['Proj_1', 'proj-2', '3-jorp', '4_jorp']
# projects = []
up_in = CardTransition(mode="push", direction="up", duration=".25")


class ListButton(Button):
    list_btn = ObjectProperty(None)


class MainManager(ScreenManager):
    main_mng = ObjectProperty()


class SubManager(ScreenManager):
    sub_mng = ObjectProperty(None)


class ProjButton(ListButton):
    main_mng = MainManager.main_mng


class MainScreen(Screen):

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

    @mainthread
    def on_enter(self, *args):
        """
        Generate list of Buttons for each Project in "projects" list
        Each Button triggers the Lvl 1 ScreenManager to change from "main_scrn" to "proj_scrn"
        https://stackoverflow.com/questions/19491286/kivy-changing-screens-in-screen-manager-with-an-on-press-event
        https://stackoverflow.com/questions/45934429/bind-a-function-to-multiple-dynamically-created-buttons-in-kivy
        https://stackoverflow.com/questions/46393737/calling-a-method-from-on-release-event-of-a-button-in-a-pop-up
        https://stackoverflow.com/questions/49265887/use-on-press-event-to-change-screen-without-kv-language-for-dynamically-created
        """
        self.main_scrn.clear_widgets()      # Clear all widgets in main_scrn
        app = App.get_running_app()         # name of running app like #homepath
        sm = app.root.ids.main_mng          # path from #homepath to #main_mng (ScreenManager Lvl 1)
        # print(sm)

        for idx, name in enumerate(projects):
            # id_ = "proj_btn_"+str(idx)
            # button = ProjButton(text=name, id=id_)
            button = ProjButton(text=name)
            button.bind(on_release=lambda *args: setattr(sm, 'current', "proj_scrn"))
            button.bind(on_release=lambda *args: setattr(sm, 'transition', up_in))
            self.ids.cont_proj_list.add_widget(button)


    def show_add_pop(self):
        add_pop()


class ProjectScreen(Screen):
    pass


class OverviewScreen(Screen):
    pass


class SampleScreen(Screen):
    pass


class add_popup(FloatLayout):
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


def add_pop():
    show = add_popup()

    addWindow = Popup(title="Add Project",
                      content=show,
                      size_hint=(None, None),
                      size=(200, 250),
                      )
    addWindow.open()


if __name__ == '__main__':
    ClassAllScreenApp().run()
