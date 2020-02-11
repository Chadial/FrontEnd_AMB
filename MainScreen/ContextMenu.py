import kivy
from kivy.app import App
from kivy.lang import Builder
import kivy.garden.contextmenu

kv = """
GridLayout:
    id: layout
    cols: 1
    AppMenu:
        id: app_menu
        top: root.height
        cancel_handler_widget: layout

        AppMenuTextItem:
            text: "Menu #1"
            ContextMenu:
                ContextMenuTextItem:
                    text: "Item #11"

    Button:
        text:   "hello"
"""

class MyApp(App):
    def build(self):
        self.title = 'Simple app menu example'
        return Builder.load_string(kv)

    def say_hello(self, text):
        print(text)
        self.root.ids['app_menu'].close_all()

if __name__ == '__main__':
    MyApp().run()