import kivy
from kivy.app import App
from kivy.lang import Builder
import kivy.garden.contextmenu

kv = "contextmenu_ex1.kv"

class MyApp(App):
    def build(self):
        self.title = 'Simple app menu example'
        return Builder.load_file(kv)

    def say_hello(self, text):
        print(text)
        self.root.ids['app_menu'].close_all()


if __name__ == '__main__':
    MyApp().run()
