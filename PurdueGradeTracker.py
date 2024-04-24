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


def get_semester_choice():
    # gather input
    choice = input("Enter Semester: ")

    # input validation
    if not os.path.exists(choice):
        print("Semester does not exist.")
        return

    return choice


def register_semester():
    # check if Semesters directory does not exist
    if not os.path.exists("Semesters"):
        os.mkdir("Semesters")

    # prompt for input
    semester_name = input("Enter semester name: ")
    # capitalize for clarity
    semester_name = semester_name.capitalize()

    # check that semester is not registered
    if os.path.exists("Semesters/" + semester_name):
        print("Semester already registered.")
    # save semester
    else:
        semester = Semester(semester_name)
        semester.save_semester_to_file()


def register_class():
    return 0


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
