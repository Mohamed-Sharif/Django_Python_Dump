import getpass

from authentication import login, register
from projects import create_project, view_projects, delete_project, edit_project
from search import search_projects_by_date, view_user_profile, donate_to_project, view_amount_raised

def main():
    print("Welcome to our crowdfunding platform!")
    while True:
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            email = input("Email: ")
            password = getpass.getpass("Password: ")
            auth = login(email,password)
            if auth:
                print("Login successful.")
                while True:
                    print("1. Create project")
                    print("2. View all projects")
                    print("3. Edit project")
                    print("4. Delete project")
                    print("5. Search projects by date")
                    print("6. View profile")
                    print("7. View amount raised for a project")
                    print("8. Logout")
                    choice = input("Enter your choice: ")

                    if choice == "1":
                        create_project(email)
                    elif choice == "2":
                        view_projects()
                    elif choice == "3":
                        edit_project(email)
                    elif choice == "4":
                        delete_project(email)
                    elif choice == "5":
                        search_projects_by_date()
                    elif choice == "6":
                        view_user_profile(email)
                    elif choice == "7":
                        title=input("Enter a project title")
                        view_amount_raised(title)
                    elif choice == "8":
                        break
                    else:
                        print("Invalid choice. Please try again.")

            else:
                print("Invalid email or password. Please try again.")
        elif choice == "2":
            register()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

main()