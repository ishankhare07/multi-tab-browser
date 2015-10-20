from gi.repository import Gtk, WebKit

class Tab(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self, orientation = Gtk.Orientation.VERTICAL)
        self.bar = Gtk.Box()
        self.pack_start(self.bar, False, True, 0)

        self.entry = Gtk.Entry()
        self.entry.set_placeholder_text('Enter the URL here e.g. http://www.google.com/')
        self.entry.connect('activate', self.loadWebPage)
        self.entry.grab_focus()

        self.goButton = Gtk.Button('➜')
        self.goButton.connect('clicked', self.loadWebPage)
        self.bar.pack_start(self.entry, True, True, 0)
        self.bar.pack_start(self.goButton, False, False, 0)

        self.webview = WebKit.WebView()
        self.webview.connect('title-changed', self.updateTitle)
        sw = Gtk.ScrolledWindow()
        sw.add(self.webview)
        self.pack_start(sw, True, True, 0)

        self.title = Gtk.Label('New Tab')

        self.show_all()

    def updateTitle(self, webview, frame, title):
        self.title.set_text(title)

    def loadWebPage(self, event):
        text = self.entry.get_text()
        self.webview.load_uri(text)

    def getTabAndLabel(self):
        box = Gtk.HBox()
        box.pack_start(self.title, True, True, 0)

        close_button    = Gtk.Button()
        close_icon      = Gtk.Image()
        close_icon.set_from_stock('gtk-close', 2)
        close_button.set_image(close_icon)
        close_button.set_relief(Gtk.ReliefStyle.NONE)

        box.pack_start(close_button, True, True, 0)

        return dict(tab=self, labelWidget=box)

class BrowserNotebook(Gtk.Notebook):
    def __init__(self):
        Gtk.Notebook.__init__(self)
        self.show_all()

    def newtTab(self):
        tabAndLabel = Tab().getTabAndLabel()
        tabAndLabel['labelWidget'].get_children()[-1].connect('clicked', self.closeTab)
        tabAndLabel['labelWidget'].show_all()

        self.append_page(tabAndLabel['tab'], tabAndLabel['labelWidget'])
        self.show_all()

    def closeTab(self, widget):
        page_num = self.get_current_page()
        self.remove_page(page_num)
