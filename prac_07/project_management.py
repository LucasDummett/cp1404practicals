from project import Project
from operator import attrgetter
import datetime

DEFAULT_FILENAME = "projects.txt"
TEST_FILE = "test.txt"


def main():
    print("Welcome to Project Management Program:")
    projects = load_projects(DEFAULT_FILENAME)
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILENAME}")
    display_menu()
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Filename: ")
            projects = load_projects(filename)
        elif choice == "S":
            filename = input("Filename: ")
            save_projects(filename, projects)
            for project in projects:
                print(project)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            # Different input prompt to Lindsay's to be more instructive for user (Year is actually yyyy not yy).
            given_date = input("Show projects that start after date (dd/mm/yyyy): ")
            date = datetime.datetime.strptime(given_date, "%d/%m/%Y").date()
            projects.sort(key=attrgetter("start_date"))
            for project in projects:
                if project.is_after(date):
                    print(project)
        elif choice == "A":
            print("Let's add a new project")
            completion_percentage, cost_estimate, name, priority, start_date = get_project_details()
            projects.append(Project(name=name, start_date=start_date, priority=priority, cost_estimate=cost_estimate,
                                    completion_percentage=completion_percentage))
        elif choice == "U":
            for i, project in enumerate(projects):
                print(f"{i} {project}")
            project_selection = projects[int(input("Project choice: "))]
            print(project_selection)
            completion_percentage_input = input("New Percentage: ")
            priority_input = input("New Priority: ")
            if completion_percentage_input != "":
                project_selection.completion_percentage = int(completion_percentage_input)
            if priority_input != "":
                project_selection.priority = int(priority_input)

        display_menu()
        choice = input(">>>").upper()
    if input("Would you like to save to projects.txt? ").upper() == "YES" or "Y":
        save_projects(DEFAULT_FILENAME, projects)
    print("Thank you for using custom-built project management software.")


def get_project_details():
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: $")
    completion_percentage = input("Percent complete: ")
    return completion_percentage, cost_estimate, name, priority, start_date


def load_projects(filename):
    """Load projects from file projects.txt."""
    projects = []
    with open(filename, "r") as infile:
        infile.readline()
        for line in infile:
            parts = line.strip().split("\t")
            projects.append(Project(name=parts[0], start_date=parts[1], priority=parts[2], cost_estimate=parts[3],
                                    completion_percentage=parts[4]))
    return projects


def save_projects(filename, projects):
    """Save projects to file."""
    with open(filename, "w") as outfile:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=outfile)
        for project in projects:
            print(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}"
                  f"\t{project.cost_estimate}\t{project.completion_percentage}", file=outfile)


def display_menu():
    """Display menu options."""
    print("""- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit""")


def display_projects(projects):
    print("Incomplete projects:")
    for project in sorted(projects):
        if project.completion_percentage != 100:
            print(project)
    print("Complete projects:")
    for project in sorted(projects):
        if project.completion_percentage == 100:
            print(project)


main()
