import json
import os
def load_projects():
    if not os.path.isfile('projects.json'):
        # Create empty list of projects if file doesn't exist
        with open('projects.json', 'w') as f:
            json.dump([], f)

    with open('projects.json', 'r') as f:
        return json.load(f)

def save_projects(projects):
    with open('projects.json', 'w') as f:
        json.dump(projects, f)

def print_projects(projects):
    print("Projects:")
    for i, project in enumerate(projects):
        print(f"{i+1}. {project['title']}")
        print(f"   Owner: {project['owner']}")
        print(f"   Details: {project['details']}")
        print(f"   Total target: {project['total_target']} EGP")
        print(f"   Start date: {project['start_date']}")
        print(f"   End date: {project['end_date']}")
        print()

