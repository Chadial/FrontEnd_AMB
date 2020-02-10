"""
https://stackoverflow.com/questions/41337143/switch-screenmanager-inside-layout
Ideas:
https://www.python-forum.de/viewtopic.php?f=4&t=46427
"""
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.clock import Clock

#just solving my weak GPU issue
from kivy import Config
Config.set('graphics', 'multisamples', '0')

kivy.require('1.9.1')


class ScreenManagement(ScreenManager):
    pass


class Init(Screen):
    pass


class Menu(Screen):
    pass


class ClassAllScreen(BoxLayout):
    pass


class ClassApp(App):

    def build(self):
        self.root = ClassAllScreen()
        return self.root


if __name__ == '__main__':
    ClassApp().run()
