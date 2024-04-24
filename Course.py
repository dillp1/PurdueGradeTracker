import os


class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.assignments = []

    def save_course_to_file(self):
        file_name = self.course_name + ".txt"

        directory = os.path.dirname(file_name)