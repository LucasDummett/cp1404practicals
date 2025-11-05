from project import Project

FILENAME = "projects.txt"
TEST_FILE = "test.txt"


def main():
    projects = load_projects(FILENAME)
    save_projects(TEST_FILE, projects)
    display_menu()
    display_projects(projects)


def load_projects(filename):
    """Load projects from file projects.txt."""
    projects = []
    with open(filename, "r", encoding="utf-8") as infile:
        infile.readline()
        for line in infile:
            parts = line.strip().split("\t")
            projects.append(Project(name=parts[0], start_date=parts[1], priority=parts[2], cost_estimate=parts[3],
                                    completion_percentage=parts[4]))
        projects.sort()
    return projects


def save_projects(filename, projects):
    """Save projects to file."""
    with open(filename, "w", encoding="utf-8") as outfile:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=outfile)
        for project in projects:
            print(f"{project.name} \t{project.start_date} \t{project.priority} \t{project.cost_estimate} "
                  f"\t{project.completion_percentage}", file=outfile)


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
            print(project)
    print("Complete projects:")
    for project in projects:
        if project.completion_percentage == 100:
            print(project)


main()
