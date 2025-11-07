"""guitar.py class
Estimate: 20 min
Actual: 15 min"""

CURRENT_YEAR = 2025
VINTAGE_AGE = 50


class Guitar:
    """Class for guitars based on details."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """String representation of guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return the age of the guitar in years."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Return boolean for whether guitar age is greater or equal to 50 years."""
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        """Enable sorting by comparing objects based on the year field. """
        return self.year < other.year
