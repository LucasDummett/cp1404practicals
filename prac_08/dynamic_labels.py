"""
Estimate: 30 mins
Actual: 25 mins
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty

FILENAME = 'dynamic_labels.kv'


class NameLabels(App):
    """Main program - Kivy app to dynamically create label for names in defined list."""
    name = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ['Child', 'Savage', 'Jeff', 'Lucas', 'Skywalker', 'Caramel Iced Latte']

    def build(self):
        """Build the Kivy GUI."""
        self.title = 'Name Labelling'
        self.root = Builder.load_file(FILENAME)
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create dynamic labels for names in defined list."""
        for name in self.names:
            name_label = Label(text=name)
            self.root.ids.name_entries.add_widget(name_label)


NameLabels().run()
