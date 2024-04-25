import os
from Semester import Semester
from Course import Course


def print_main_menu(current_semester):
    print("-= Main Menu =-")
    print(f"Current Semester: {current_semester}\n")
    print("1. Change Current Semester")
    print("2. Add Grade")
    print("3. Register Course")
    print("4. Register Semester")
    print("5. Exit")


def get_main_menu_choice(current_semester):
    while True:
        try:
            # gather input
            choice = int(input("\nChoice: "))

            # input validation
            if 1 <= choice <= 5:
                return choice
            else:
                print("Please enter 1, 2, 3, 4, or 5.\n")
                print_main_menu(current_semester)

        except ValueError:
            print("Please enter 1, 2, 3, 4, or 5.\n")
            print_main_menu(current_semester)


def get_semester_choice():
    while True:
        # gather input
        choice = input("Enter Semester: ")

        # build file path
        file_path = os.path.join("Semesters", choice)

        # input validation
        if not os.path.exists(file_path):
            print("Semester does not exist.\n")
        else:
            return choice


def get_credit_hours():
    while True:
        # gather input
        credit_hours = int(input("Enter Credit Hours: "))

        if credit_hours < 0:
            print("Credit Hours cannot be negative.\n")
        else:
            return credit_hours


def register_semester():
    # prompt for input
    semester_name = input("Enter Semester Name: ")
    # capitalize for clarity
    semester_name = semester_name.capitalize()

    #create semesters directory
    if not os.path.exists("Semesters"):
        os.mkdir("Semesters")

    # check that semester is not registered
    if os.path.exists("Semesters/" + semester_name):
        print("Semester already registered.\n")
    # save semester
    else:
        semester = Semester(semester_name)
        semester.save_semester_to_file()
        print(f"{semester_name} semester has been registered!\n")


def register_course():
    # check that at least one semester has been registered
    if not os.path.exists('Semesters'):
        print("No semesters have been registered yet.\n")
        return

    # prompt for semester
    semester_name = get_semester_choice()

    # prompt for course name
    course_name = input("Enter Course Name: ") + '.txt'

    # construct file path
    file_path = os.path.join("Semesters", semester_name, course_name)

    if os.path.exists(file_path):
        print("Course already exist.\n")
    else:
        course = Course(course_name)
        semester = Semester(semester_name)

        semester.add_course_to_semester(course)
        course.save_course_to_file(file_path)

        print("Course registered!\n")


def main():
    print("Welcome to Purdue Grade Tracker!")

    # declare variables
    current_semester = 'NONE'

    # main loop
    while True:
        # get choice from main menu
        print_main_menu(current_semester)
        choice = get_main_menu_choice(current_semester)

        # choice 1 - Change Current Semester
        if choice == 1:
            if not os.path.exists('Semesters'):
                print("\nNo semesters have been registered yet.\n")
            else:
                current_semester = get_semester_choice()
                print(f"Current semester has been changed to {current_semester}.\n")

        # choice 2 - Add Grade
        elif choice == 2:
            return 0

        # choice 3 - Register Course
        elif choice == 3:
            register_course()

        # choice 4 - Register Semester
        elif choice == 4:
            register_semester()

        # choice 5 - Quit
        else:
            print("Goodbye")
            break


if __name__ == "__main__":
    main()
