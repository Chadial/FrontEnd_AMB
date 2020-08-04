"""
https://stackoverflow.com/questions/41337143/switch-screenmanager-inside-layout
Ideas:
https://www.python-forum.de/viewtopic.php?f=4&t=46427
"""
from kivy import Config

win_px = 960
Config.set('graphics', 'width', str(win_px))
Config.set('graphics', 'height', str(int(win_px * 0.618)))
Config.set('graphics', 'minimum_width', str(int(win_px * 0.6)))
Config.set('graphics', 'minimum_height', str(int(win_px * 0.618 * .5)))

import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty, ListProperty, StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, CardTransition
from kivy.clock import Clock, mainthread
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner

import kivy.garden.contextmenu
# https://stackoverflow.com/questions/55133377/pycharm-error-kivy-garden-knob-import-successfully-but-not-active-on-script
# https://kivy.org/doc/stable/api-kivy.garden.html

from kivy import Config

Config.set('graphics', 'multisamples', '0')

""" kv File """
Builder.load_file('maingui.kv')

""" Constants """
up_in = CardTransition(mode="push", direction="up", duration=".25")

""" Variables """
prj_list = ['Proj_1', 'proj-2', '3-jorp', '4_jorp']
# prj_list = []

""" Layouts """
class ProjectGridLayout(GridLayout):

    def show_labels(self, var):
        self.clear_widgets()

        self.main_scrn.clear_widgets()  # Clear all widgets in main_scrn
        app = App.get_running_app()  # name of running app like #homepath
        sm = app.root.ids.main_mng  # path from #homepath to #main_mng (ScreenManager Lvl 1)

        for idx, name in enumerate(var):
            button = ProjButton(text=name)
            button.bind(on_release=lambda *args: setattr(sm, 'current', "proj_scrn"))
            button.bind(on_release=lambda *args: setattr(sm, 'transition', up_in))
            self.ids.cont_proj_list.add_widget(button)


class SampleGridLayout(GridLayout):
    pass


class MainManager(ScreenManager):
    main_mng = ObjectProperty()


class SubManager(ScreenManager):
    sub_mng = ObjectProperty()


class ListButton(Button):
    pass


class ProjButton(ListButton):
    main_mng = MainManager.main_mng


""" DropDowns """
class ProjListSpinner(Spinner):
    """
    https://stackoverflow.com/questions/39593544/changing-kivy-spinner-values-dynamically
    """
    pass


""" Popups """
class ope_prj_pop(FloatLayout):
    prj_list = ListProperty()

    def __init__(self, **kwargs):
        super(ope_prj_pop, self).__init__(**kwargs)
        self.prj_list = prj_list


class add_prj_pop(FloatLayout):
    prj_list = ListProperty()

    def __init__(self, **kwargs):
        super(add_prj_pop, self).__init__(**kwargs)
        self.prj_list = prj_list

    def add_prj_list(self, val):
        if not check_str(val):
            print("False Name given")
        elif check_str(val):
            prj_list.append(val)
        return prj_list


class dup_prj_pop(FloatLayout):
    prj_list = ListProperty()

    def __init__(self, **kwargs):
        super(dup_prj_pop, self).__init__(**kwargs)
        self.prj_list = prj_list

    def dup_prj_list(self, val):
        prj_list.remove(val)
        print(prj_list)
        return prj_list


class del_prj_pop(FloatLayout):
    prj_list = ListProperty()

    def __init__(self, **kwargs):
        super(del_prj_pop, self).__init__(**kwargs)
        self.prj_list = prj_list

    def del_prj_list(self, val):
        pop_pop(4)
        return confirm_pop.choice(val, 0)
        # return con_del_pop.delete_prj(val)
        # return c

    def del_val(self, val):
        prj_list.remove(val)
        return prj_list


class confirm_pop(FloatLayout):
    val_1 = ObjectProperty()
    val_2 = StringProperty('')
    """ Popup to confirm the deletion """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.val_1 = val
        self.voice = self.voice

    def choice(self, val, voice):
        if voice == 0:
            self.ids.conf_text.text = "Set Text"
            del_prj_pop.del_val(val)
        else:
            pass


""" Screens """
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
        https://stackoverflow.com/questions/35044166/how-do-i-add-buttons-that-are-dynamically-created-in-pure-python-to-a-kivy-layou
        """
        if not prj_list:
            self.main_scrn.clear_widgets()  # Clear all widgets in main_scrn
            self.ids.ope_prj_btn.disabled = True
            self.ids.dup_prj_btn.disabled = True
            self.ids.del_prj_btn.disabled = True
        else:
            self.main_scrn.clear_widgets()  # Clear all widgets in main_scrn
            self.ids.ope_prj_btn.disabled = False
            self.ids.dup_prj_btn.disabled = False
            self.ids.del_prj_btn.disabled = False
            app = App.get_running_app()  # name of running app like #homepath
            sm = app.root.ids.main_mng  # path from #homepath to #main_mng (ScreenManager Lvl 1)

            for idx, name in enumerate(prj_list):
                button = ProjButton(text=name)
                button.bind(on_release=lambda *args: setattr(sm, 'current', "proj_scrn"))
                button.bind(on_release=lambda *args: setattr(sm, 'transition', up_in))
                self.ids.cont_proj_list.add_widget(button)

    def show_pop(self, window):
        """ Comment """
        pop_pop(window)


class ProjectScreen(Screen):
    pass


class OverviewScreen(Screen):
    pass


class SampleScreen(Screen):
    pass


""" App Elements """


class Header(BoxLayout):
    head = ObjectProperty(None)


class Footer(BoxLayout):
    pass


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

def delete_prj_item(item):
    prj_list.remove(item)
    return prj_list


def check_str(val):
    if val in prj_list:
        print("{} already exist".format(val))
        return False
    elif not val:
        print("No Name given.")
        return False
    elif val.isspace():
        print("No Name given.")
        return False
    elif val.isdigit():
        print("Name without letters given.")
        return False
    elif len(val) < 5:
        print("Name has less than 5 characters.")
        return False
    elif len(val) > 16:
        print("Name has more than 16 characters.")
        return False
    elif val[0].isdigit() or val[0].isspace():
        print("First character must be a letter.")
        return False
    else:
        return True


def pop_pop(window):
    if window == 0:
        title_ = "Open Project"
        pop_ = ope_prj_pop()
        size_ = (300, 500)
        size_hint_ = (.5, .5)
    elif window == 1:
        title_ = "Add Project"
        pop_ = add_prj_pop()
        size_ = (300, 500)
        size_hint_ = (.5, .5)
    elif window == 2:
        title_ = "Duplicate Project"
        pop_ = dup_prj_pop()
        size_ = (300, 500)
        size_hint_ = (.5, .5)
    elif window == 3:
        title_ = "Delete Project"
        pop_ = del_prj_pop()
        size_ = (300, 500)
        size_hint_ = (.5, .5)
    elif window == 4:
        title_ = "Confirm deletion"
        pop_ = confirm_pop()
        size_ = (300, 500)
        size_hint_ = (.5, .5)

    win_dow = Popup(title=title_,
                    content=pop_,
                    # size_hint=(None, None),
                    size_hint=size_hint_,
                    auto_dismiss=False,
                    # size=size_,
                    )
    """ https://stackoverflow.com/questions/46948218/kivy-button-in-popup-not-calling-function """
    pop_.ids["okay"].bind(on_release=win_dow.dismiss)
    pop_.ids["cancel"].bind(on_release=win_dow.dismiss)
    win_dow.open()


if __name__ == '__main__':
    ClassAllScreenApp().run()
