"""
https://www.geeksforgeeks.org/python-file-chooser-in-kivy/
"""

import kivy

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Filechooser(BoxLayout):
    def select(self, *args):
        try:
            self.input.text = args[1][0]
        except:
            pass


class FileApp(App):
    def build(self):
        return Filechooser()


if __name__ == "__main__":
    FileApp().run()

