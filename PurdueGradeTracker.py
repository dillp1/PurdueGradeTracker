import os
from Semester import Semester
from Course import Course


def print_main_menu():
    print("Menu:")
    print("1. Add Grade")
    print("2. Register Course")
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
    while True:
        # gather input
        choice = input("Enter Semester: ")

        # build file path
        file_path = os.path.join("Semesters", choice)

        # input validation
        if not os.path.exists(file_path):
            print("Semester does not exist.")
        else:
            return choice


def get_credit_hours():
    while True:
        # gather input
        credit_hours = int(input("Enter Credit Hours: "))

        if credit_hours < 0:
            print("Credit Hours cannot be negative.")
        else:
            return credit_hours


def register_semester():
    # prompt for input
    semester_name = input("Enter Semester Name: ")
    # capitalize for clarity
    semester_name = semester_name.capitalize()

    # check that semester is not registered
    if os.path.exists("Semesters/" + semester_name):
        print("Semester already registered.")
    # save semester
    else:
        semester = Semester(semester_name)
        semester.save_semester_to_file()
        print(f"{semester_name} semester has been registered!")


def register_course():
    # prompt for input
    semester_name = get_semester_choice()

    # prompt for course name
    course_name = input("Enter Course Name: ")

    # construct file path
    file_path = os.path.join("Semesters", semester_name, course_name)

    if os.path.exists(file_path):
        print("Course already exist.")
    else:
        course = Course(course_name)
        semester = Semester(semester_name)
        semester.add_course_to_semester(course)
        print("Course registered!")


def main():
    print("Welcome to Purdue Grade Tracker!")

    # build list of semesters
    semesters = []
    current_directory = "Semesters"

    if not os.path.exists(current_directory):
        os.mkdir(current_directory)

    all_semesters = os.listdir(current_directory)
    for semester in all_semesters:
        if os.path.isdir(os.path.join(current_directory, semester)):
            semesters.append(semester)

    # main loop
    while True:
        # get choice from main menu
        print_main_menu()
        choice = get_main_menu_choice()

        # choice 1 - Add Grade
        if choice == 1:
            return 0

        # choice 2 - Register Course
        elif choice == 2:
            register_course()

        # choice 3 - Register Semester
        elif choice == 3:
            register_semester()

        # choice 4 - Quit
        else:
            print("Goodbye")
            break


if __name__ == "__main__":
    main()
