"""
project.py
Estimate: 50 mins
Actual: 30 mins
"""

import datetime


class Project:
    """Class representing a project."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialise a project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __lt__(self, other):
        """Enable sorting by comparing objects based on the priority field. """
        return self.priority < other.priority

    def __str__(self):
        """String representation of a project."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%")

    def is_after(self, given_date):
        """Determine if project start date is equal to or after given date."""
        return self.start_date >= given_date

    def detail_to_row(self) -> str:
        """Return a formatted string with tabbed project fields."""
        return (f"{self.name}\t{self.start_date.strftime('%d/%m/%Y')}\t"
                f"{self.priority}\t{self.cost_estimate}\t{self.completion_percentage}")
