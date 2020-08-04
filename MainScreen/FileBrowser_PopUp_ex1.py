"""
https://stackoverflow.com/questions/48259400/kivy-using-popup-open
https://stackoverflow.com/questions/32439330/add-filebrowser-in-kivy
https://stackoverflow.com/questions/53734589/kivy-how-to-use-filebrowser-properly-inside-of-a-popup
"""

from kivy.app import App
from kivy.uix.popup import Popup
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.filebrowser import FileBrowser
from kivy.properties import StringProperty, ObjectProperty

Builder.load_file('filebrowser_popup_ex1.kv')

class FileBrowserPopup(Popup):
    title = StringProperty()
    path = StringProperty()
    choice = StringProperty()

    def __init__(self, title, path, **kwargs):
        super(FileBrowserPopup, self).__init__(**kwargs)
        self.set_properties(title, path)

    def set_properties(self, title, path):
        self.title = title
        self.path = path

    def get_choice(self):
        print(self.choice.text)
        return self.choice


class SaveAs(BoxLayout):
    teinp = ObjectProperty()

    def on_call_popup(self):
        pop = FileBrowserPopup("File Manager", "D:/")
        pop.open()
        pop.bind(on_success=self.next_step)

    def next_step(self, popup):
        self.teinp.text = popup.get_choice()
        print(self.teinp.text)


class ExplorerApp(App):

    def build(self):
        return SaveAs()


if __name__ == '__main__':
    ExplorerApp().run()
