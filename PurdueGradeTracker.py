import os
from Semester import Semester


def print_main_menu():
    print("Menu:")
    print("1. Add Grade")
    print("2. Register Class")
    print("3. Register Semester")
    print("4. Exit")


def get_main_menu_choice():
    while True:
        try:
            # gather input
            choice = int(input("Choice: "))

            # input validation
            if 1 <= choice <= 4:
                return choice
            else:
                print("Please enter 1, 2, 3, or 4.")
                print_main_menu()

        except ValueError:
            print("Please enter 1, 2, 3, or 4.")
            print_main_menu()


def save_semester_to_file(semester):
    # get folder name
    folder_name = semester.semester_name

    # create file directory for semester
    os.mkdir(folder_name)
    print(f"{semester.semester_name} semester has been registered!")


def register_semester():
    # prompt for input
    semester_name = input("Enter semester name: ")
    # capitalize for clarity
    semester_name = semester_name.capitalize()

    # check that semester is not registered
    if os.path.exists(semester_name):
        print("Semester already registered.")
    # save semester
    else:
        semester = Semester(semester_name)
        save_semester_to_file(semester)


def main():
    print("Welcome to Purdue Grade Tracker!")

    # main loop
    while True:
        # get choice from main menu
        print_main_menu()
        choice = get_main_menu_choice()

        # choice 1 - Add Grade
        if choice == 1:
            return 0

        # choice 2 - Register Class
        elif choice == 2:
            return 0

        # choice 3 - Register Semester
        elif choice == 3:
            register_semester()

        # choice 4 - Quit
        else:
            print("Goodbye")
            break


if __name__ == "__main__":
    main()
