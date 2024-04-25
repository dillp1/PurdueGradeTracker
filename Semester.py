import os


class Semester:
    def __init__(self, semester_name):
        self.semester_name = semester_name
        self.courses = []

    def save_semester_to_file(self):
        # get folder and file names
        folder_name = self.semester_name
        file_name = folder_name + ".txt"

        # create file directory for semester
        semester_directory = os.path.join("Semesters", folder_name)
        os.mkdir(semester_directory)

        # create file path
        file_path = os.path.join(semester_directory, file_name)

        # write new file to store semester data
        with open(file_path, "w") as file:
            file.write(self.semester_name + "\n")

    def add_course_to_semester(self, course):
        self.courses.append(course)
