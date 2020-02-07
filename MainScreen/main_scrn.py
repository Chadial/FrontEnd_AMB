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
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
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


class MainMenuApp(App):
    def build(self):
        return MainMenu()


if __name__ == "__main__":
    MainMenuApp().run()
