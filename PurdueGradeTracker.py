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
            return 0

        # choice 4 - Quit
        else:
            print("Goodbye")
            break


if __name__ == "__main__":
    main()
