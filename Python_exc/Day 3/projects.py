import datetime
from helpers import load_projects, save_projects, print_projects

# define a class to represent a project
class Project:
    def __init__(self, title, details, target_amount, start_date, end_date, owner, amount_raised=0, backers=None):
        self.title = title
        self.details = details
        self.target_amount = target_amount
        self.start_date = start_date
        self.end_date = end_date
        self.owner = owner
        self.amount_raised = amount_raised
        self.backers = backers or []

def create_project(email):
    # Load existing projects from file
    projects = load_projects()

    # Get project details from user
    title = input("Enter the project title: ")
    details = input("Enter the project details: ")
    target = float(input("Enter the target amount: "))
    start_date_str = input("Enter the start date (YYYY-MM-DD): ")
    end_date_str = input("Enter the end date (YYYY-MM-DD): ")

    try:
        start_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d').date()
        end_date = datetime.datetime.strptime(end_date_str, '%Y-%m-%d').date()
    except ValueError:
        print("Invalid date format. Please use the format YYYY-MM-DD.")
        return

    if end_date <= start_date:
        print("Invalid date range. The end date must be after the start date.")
        return

    # Create new project and add it to the list of projects
    project = Project(title, details, target, start_date, end_date, email)
    projects.append(project.__dict__)

    # Save updated list of projects to file
    save_projects(projects)
    print("Project created successfully.")

def view_projects():
    # Load existing projects from file
    projects = load_projects()

    # Print a table of all projects
    print("Projects:")
    for project_dict in projects:
        project = Project(**project_dict)
        print(project.title)
        print("Target amount:", project.target_amount)
        print("Start date:", project.start_date)
        print("End date:", project.end_date)
        print("Amount raised:", project.amount_raised)
        print("Backers:", project.backers)
        print()

def edit_project(email):
    # Load existing projects from file
    projects = load_projects()

    # Find the index of the project with the given email as owner
    index = None
    for i, p in enumerate(projects):
        if p['owner'] == email:
            index = i
            break

    # If a project was found, update its details and save to file
    if index is not None:
        project_dict = projects[index]
        project = Project(**project_dict)

        print("Current project details:")
        print("Title:", project.title)
        print("Details:", project.details)
        print("Target amount:", project.target_amount)
        print("Start date:", project.start_date)
        print("End date:", project.end_date)

        # Get updated details from user
        print("Enter new project details (or leave blank to keep current value):")
        title = input("Title: ") or project.title
        details = input("Details: ") or project.details
        target = float(input("Target amount: ")) or project.target_amount
        start_date = input("Start date (YYYY-MM-DD): ") or project

def edit_project(email):
    # Load existing projects from file
    projects = load_projects()

    # Find the index of the project with the given email as owner
    index = None
    for i, p in enumerate(projects):
        if p['owner'] == email:
            index = i
            break

    # If a project was found, update its details and save to file
    if index is not None:
        project_dict = projects[index]
        project = Project(**project_dict)

        print("Current project details:")
        print("Title:", project.title)
        print("Details:", project.details)
        print("Target amount:", project.target_amount)
        print("Start date:", project.start_date)
        print("End date:", project.end_date)

        # Get updated details from user
        print("Enter new project details (or leave blank to keep current value):")
        title = input("Title: ") or project.title
        details = input("Details: ") or project.details
        target = float(input("Target amount: ")) or project.target_amount
        start_date_str = input("Start date (YYYY-MM-DD): ") or str(project.start_date)
        end_date_str = input("End date (YYYY-MM-DD): ") or str(project.end_date)

        try:
            start_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.datetime.strptime(end_date_str, '%Y-%m-%d').date()
        except ValueError:
            print("Invalid date format. Please use the format YYYY-MM-DD.")
            return

        if end_date <= start_date:
            print("Invalid date range. The end date must be after the start date.")
            return

        # Update the project details and save to file
        project.title = title
        project.details = details
        project.target_amount = target
        project.start_date = start_date
        project.end_date = end_date
        projects[index] = project.__dict__
        save_projects(projects)
        print("Project updated successfully.")
    else:
        print("No project found for the given email.")

def delete_project(email):
    # Load existing projects from file
    projects = load_projects()

    # Find the index of the project with the given email as owner
    index = None
    for i, p in enumerate(projects):
        if p['owner'] == email:
            index = i
            break

    # If a project was found, delete it and save to file
    if index is not None:
        del projects[index]
        save_projects(projects)
        print("Project deleted successfully.")
    else:
        print("No project found for the given email.")
