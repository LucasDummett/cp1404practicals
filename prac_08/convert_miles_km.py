"""
Estimate: 60 mins
Actual:  mins
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty



class MileToKmApp(App):
    """MileToKmApp is a Kivy App for converting miles to kilometres."""
    output_km = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root


MileToKmApp().run()
