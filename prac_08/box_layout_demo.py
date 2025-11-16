"""
Estimated: 15 mins
Actual: 20 mins
"""
from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Build box layout for demo."""
    def build(self):
        """Initialise the title and the builder kivy file."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Display the named entered to user on a label."""
        print('Test')
        self.root.ids.output_label.text = f"Hello, {self.root.ids.input_name.text}"

    def clear_greet(self):
        """Clear the labels for input and output text."""
        self.root.ids.output_label.text = ""
        self.root.ids.input_name.text = " "


BoxLayoutDemo().run()
