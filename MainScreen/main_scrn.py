"""
From Samuel Courses - "Building a POS System with Python and Kivy" Playlist on Youtube
https://www.youtube.com/watch?v=53Jtx3v9ZZU&list=PLW062AfleDZbWPQXjyMeLOlcL8aQ4aLeP&index=1
"""
from kivy import Config
win_px = 960
Config.set('graphics', 'width', str(win_px))
Config.set('graphics', 'height', str(int(win_px*0.618)))
Config.set('graphics', 'minimum_width', str(int(win_px*0.5)))
Config.set('graphics', 'minimum_height', str(int(win_px*0.618*.5)))

from kivy.app import App
from kivy.lang import Builder

from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.behaviors import FocusBehavior

from kivy.properties import NumericProperty, StringProperty, BooleanProperty



from kivy.core.window import Window, WindowBase

Builder.load_file('main_scrn.kv')


class MainMenu(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def validate_user(self):
        # self.ids -- list of all ids in kivy file called SigninApp (signin.kv)
        user = self.ids.username_field
        pwds = self.ids.pwd_field
        info = self.ids.info

        uname = user.text
        passw = pwds.text

        if uname == '' or passw == '':
            info.text = '[color=#FF0000]Username and/ or Password required[/color]'
        else:
            if uname == 'admin' and passw == 'admin':
                info.text = '[color=#00FF00]Logged In successfully[/color]'
                self.parent.parent.current = "scrn_admin"
            else:
                info.text = '[color=#FF0000]Invalid Username and/ or Password[/color]'


class ProjectList(RecycleView):
    def __init__(self, proj_list=[], *args, **kwargs):
        super(ProjectList, self).__init__(*args, **kwargs)

        self.data = []
        for idx, proj in enumerate(proj_list):
            self.data.append({'text': proj})


class SelectableLabel(RecycleView, Label):
    def __init__(self, ):
        pass




class MainMenuApp(App):
    def build(self):
        return MainMenu()


if __name__ == "__main__":
    MainMenuApp().run()
