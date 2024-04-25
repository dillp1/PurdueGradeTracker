import os


class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.assignments = []

    def save_course_to_file(self, file_path):
        # create new file
        with open(file_path, 'w') as file:
            # write name to file
            file.write(self.course_name)
