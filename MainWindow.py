from gi.repository import Gtk, WebKit
import Notebook

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title='Browser')
        self.connect('destroy', Gtk.main_quit)
        self.notebook = Notebook.BrowserNotebook()
        self.notebook.newtTab()

        self.add(self.notebook)
        self.resize(1000, 700)

if __name__ == "__main__":
    window = MainWindow()
    window.show_all()
    print('Tests finished successfully')
