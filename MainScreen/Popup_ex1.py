"""
https://stackoverflow.com/questions/48259400/kivy-using-popup-open
"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.properties import StringProperty, ObjectProperty
from kivy.lang.builder import Builder

Builder.load_file('popup_ex1.kv')

class TextInputPopup(Popup):
    title = StringProperty()
    label = StringProperty()
    answer = ObjectProperty()

    def __init__(self, title, label, **kwargs):
        super(TextInputPopup, self).__init__(**kwargs)
        self.set_description(title, label)

    def set_description(self, title, label):
        self.title = title
        self.label = label

    def get_answer(self):
        return self.answer.text


class SaveAs(BoxLayout):
    teinp = ObjectProperty()

    def on_call_popup(self):
        poti = TextInputPopup('File Manager', 'Name')
        poti.open()
        poti.bind(on_dismiss=self.next_step)

    def next_step(self, popup):
        self.teinp.text = popup.get_answer()


class ExplorerApp(App):

    def build(self):
        return SaveAs()


if __name__ == '__main__':
    ExplorerApp().run()