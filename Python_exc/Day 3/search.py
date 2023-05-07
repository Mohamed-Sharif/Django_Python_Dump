import datetime
from helpers import load_projects, save_projects, print_projects

def search_projects_by_date():
    
    projects = load_projects()
    date_str = input("Enter the date (YYYY-MM-DD) to search for projects: ")
    try:
        date = datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        print("Invalid date format. Please use the format YYYY-MM-DD.")
        return

    results = []
    for p in projects:
        start_date = datetime.strptime(p['start_date'], '%Y-%m-%d')
        end_date = datetime.strptime(p['end_date'], '%Y-%m-%d')
        if start_date <= date <= end_date:
            results.append(p)

    if not results:
        print("No projects found for the given date.")
    else:
        print_projects(results)



def view_user_profile(email):
    projects = load_projects()
    user_projects = [p for p in projects if p['owner'] == email]
    if not user_projects:
        print("No projects found for the given email.")
    else:
        print_projects(user_projects)

def donate_to_project():
    projects = load_projects()
    print_projects(projects)
    project_index = int(input("Enter the number of the project to donate to: "))
    amount = int(input("Enter the amount to donate: "))

    # Update the amount raised for the selected project
    projects[project_index]['amount_raised'] += amount
    save_projects(projects)
    print("Donation received. Thank you for your support!")

def view_amount_raised(title):
    # Load existing projects from file
    projects = load_projects()

    # Find the project with the given title
    project = None
    for p in projects:
        if p['title'] == title:
            project = p
            break

    # If a project was found, print the amount raised
    if project is not None:
        print("Amount raised for " + title + ": " + str(project['amount_raised']))
    else:
        print("No project found with the title " + title)

