"""
Estimate: 50 mins
Actual: 30 mins
"""

import datetime

COMPLETE = 100


class Project:
    """Class representing a project."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialize a project instances."""
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        """String representation of a project."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Sort projects by priority."""
        return self.priority < other.priority
