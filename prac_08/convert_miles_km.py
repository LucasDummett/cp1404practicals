"""
Estimate: 60 mins
Actual: 75 mins
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM_RATIO = 1.609344


class MileToKmApp(App):
    """MileToKmApp is a Kivy App for converting miles to kilometres."""
    output_km = StringProperty()

    def build(self):
        """Build the Kivy app from the .kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_distance_conversion(self):
        """Calculate kilometers from mile input (user input or increment)."""
        number_of_miles = self.get_valid_input()
        number_of_kilometers = number_of_miles * MILES_TO_KM_RATIO
        self.root.ids.output_label.text = str(number_of_kilometers)

    def handle_increment(self, increment):
        """Increment the string input with button pressed and update the label value."""
        number_of_miles = self.get_valid_input() + increment
        self.root.ids.input_miles.text = str(number_of_miles)
        self.handle_distance_conversion()

    def get_valid_input(self):
        """Convert input to float, returning 0 if invalid input."""
        try:
            return float(self.root.ids.input_miles.text)
        except ValueError:
            return 0


MileToKmApp().run()
