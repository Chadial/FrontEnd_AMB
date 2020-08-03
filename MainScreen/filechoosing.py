"""
https://www.geeksforgeeks.org/python-file-chooser-in-kivy/
"""

# Program to explain how to use File chooser in kivy

# import kivy module
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
kivy.require('1.9.0')

# create the layout class
class Filechooser(BoxLayout):
    def select(self, *args):
        try:
            self.xhit.text = args[1][0]
            print(args[0])
            print(args[0][1])
            print(args[1])
        except:
            pass


# Create the App class
class FileApp(App):
    def build(self):
        return Filechooser()

    # run the App


if __name__ == '__main__':
    FileApp().run()
