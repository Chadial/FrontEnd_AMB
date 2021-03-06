"""
http://kivy-garden.github.io/garden.filebrowser/api.html
https://stackoverflow.com/questions/32439330/add-filebrowser-in-kivy
"""
from kivy.app import App
from os.path import sep, expanduser, isdir, dirname
from kivy.garden.filebrowser import FileBrowser

class TestApp(App):

    def build(self):
        user_path = expanduser('~') + sep + 'Documents'
        browser = FileBrowser(select_string='Select',
                              favorites=[(user_path, 'Documents')],
                              path=user_path)
        browser.bind(on_success=self._fbrowser_success,
                     on_canceled=self._fbrowser_canceled)
        return browser

    def _fbrowser_canceled(self, instance):
        print('cancelled, Close self.')
        App.stop(self)

    def _fbrowser_success(self, instance):
        print(instance.selection)
        App.stop(self)


if __name__ == '__main__':
    TestApp().run()
