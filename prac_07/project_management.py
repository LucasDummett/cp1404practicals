from project import Project
from operator import attrgetter
import datetime

DEFAULT_FILENAME = "projects.txt"
TEST_FILE = "test.txt"
COMPLETE_PERCENTAGE = 100


def main():
    current_filename = DEFAULT_FILENAME
    print("Welcome to Project Management Program:")
    projects = load_projects(current_filename)
    print(f"Loaded {len(projects)} projects from {current_filename}")

    display_menu()
    choice = input(">>> ").strip().upper()
    while choice != "Q":
        if choice == "L":
            current_filename = input("Filename: ").strip()
            projects = load_projects(current_filename)

        elif choice == "S":
            current_filename = input("Filename: ").strip()
            save_projects(current_filename, projects)
            print(f"Saved {len(projects)} projects to {current_filename}")

        elif choice == "D":
            display_projects(projects)

        elif choice == "F":
            # Different input prompt to Lindsay's to be more instructive for user (Year is actually yyyy not yy).
            given_date = input("Show projects that start after date (dd/mm/yyyy): ").strip()
            threshold_date = datetime.datetime.strptime(given_date, "%d/%m/%Y").date()

            for project in sorted(projects, key=attrgetter("start_date")):
                if project.is_after(threshold_date):
                    print(project)

        elif choice == "A":
            print("Let's add a new project")
            completion_percentage, cost_estimate, name, priority, start_date = get_project_details()
            projects.append(Project(name=name, start_date=start_date, priority=priority, cost_estimate=cost_estimate,
                                    completion_percentage=completion_percentage))
        elif choice == "U":
            for i, project in enumerate(projects):
                print(f"{i} {project}")
            try:
                project_selection = projects[int(input("Project choice: ").strip())]
            except (ValueError, IndexError):
                print("Invalid Selection")
                display_menu()
                choice = input(">>> ").strip().upper()
                continue

            print(project_selection)
            completion_percentage_input = input("New Percentage: ").strip()
            priority_input = input("New Priority: ").strip()
            if completion_percentage_input != "":
                project_selection.completion_percentage = int(completion_percentage_input)
            if priority_input != "":
                project_selection.priority = int(priority_input)

        display_menu()
        choice = input(">>>").strip().upper()

    if input(f"Would you like to save to {current_filename} ").strip().upper() in ["YES", "Y"]:
        save_projects(current_filename, projects)
    print("Thank you for using custom-built project management software.")


def get_project_details():
    name = input("Name: ").strip()
    start_date = input("Start date (dd/mm/yyyy): ").strip()
    priority = input("Priority: ").strip()
    cost_estimate = input("Cost estimate: $").strip()
    completion_percentage = input("Percent complete: ").strip()
    return completion_percentage, cost_estimate, name, priority, start_date


def load_projects(filename):
    """Load projects from file projects.txt."""
    projects = []
    with open(filename, "r", encoding="utf-8") as infile:
        infile.readline()  # Skip header.
        for line in infile:
            parts = line.strip().split("\t")
            projects.append(Project(name=parts[0], start_date=parts[1], priority=parts[2], cost_estimate=parts[3],
                                    completion_percentage=parts[4]))
    return projects


def save_projects(filename, projects):
    """Save projects to file."""
    with open(filename, "w", encoding="utf-8") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            print(project.detail_to_row(), file=out_file)


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
        if project.completion_percentage != COMPLETE_PERCENTAGE:
            print(f"\t{project}")
    print("Completed projects:")
    for project in sorted(projects):
        if project.completion_percentage == COMPLETE_PERCENTAGE:
            print(f"\t{project}")


main()
