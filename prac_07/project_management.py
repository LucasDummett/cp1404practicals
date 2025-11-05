from project import Project

FILENAME = "projects.txt"
TEST_FILE = "test.txt"


def main():
    print("Welcome to Project Management Program:")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")
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
        display_menu()
        choice = input(">>>").upper()


def load_projects(filename):
    """Load projects from file projects.txt."""
    projects = []
    with open(filename, "r") as infile:
        infile.readline()
        for line in infile:
            parts = line.strip().split("\t")
            projects.append(Project(name=parts[0], start_date=parts[1], priority=parts[2], cost_estimate=parts[3],
                                    completion_percentage=parts[4]))
        projects.sort()
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
    for project in projects:
        if project.completion_percentage != 100:
            print(str(project))
    print("Complete projects:")
    for project in projects:
        if project.completion_percentage == 100:
            print(str(project))


main()
