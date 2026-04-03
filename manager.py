"""Student Manager Module
Core module for managing students, classrooms, and subjects.

Contain classes and methods to:
- add, update, and remove students
- manage classrooms and their students
- handle subjects, grades, and statistics

Expect data structure:
- students = {student_id:{"name": student_name, "prename": student_prename,
 "classroom": student_classroom, "grades":{"subject_id": grade,...}}, ...}
- classrooms = {classroom_id:{"name": classroom_name}, ...}
- subjects = {subject_id:{"name": subject_name, "weight": subject_weight}, ...}

All methods receive the data dictionaries as parameters to ensure modularity
and  clean code."""


class Student():
    """Represents a student with personal information and grades"""

    def __init__(self, student_id, student_name, student_prename, student_classroom):
        """Initializes a student with his ID, name, prename and classroom"""
        self.id = student_id
        self.name = student_name
        self.prename = student_prename
        self.classroom = student_classroom

    def student_grades(self, students):
        """Returns all the student's grades in a dictionary"""
        return students[self.id]["grades"]

    def student_average(self, students, subjects):
        """Returns the average of the student"""
        total_notes = 0
        total_credits = 0
        for subject_id in list(students[self.id]["grades"].keys()):
            total_notes += (students[self.id]["grades"][subject_id] *
                            subjects[subject_id]["weight"])
            total_credits += subjects[subject_id]["weight"]
        return total_notes / total_credits

    def modify_grade(self, subject_id, new_grade, students):
        """Add or Updates a student's grade"""
        students[self.id]["grades"][subject_id] = new_grade

    def delete_grade(self, subject_id, students):
        """Delete a student's grade"""
        del students[self.id]["grades"][subject_id]

    def modify_name(self, new_name, students):
        """Updates a student's name"""
        students[self.id]["name"] = new_name

    def modify_prename(self, new_prename, students):
        """Updates a student's prename"""
        students[self.id]["prename"] = new_prename

    def display_info(self, students):
        """Displays information about the student in a dictionary"""
        return students[self.id]


class Subject():
    """Represents a subject with its associated grades"""

    def __init__(self, subject_name, subject_id, subject_weight):
        """Initializes a subject with ID , name and weight"""
        self.name = subject_name  # name of the subject
        self.id = subject_id  # ID number of the subject
        self.weight = subject_weight # subject weight

    def all_grades(self, students):
        """Returns all grades for a subject"""
        return [
            students[student_id]["grades"][self.id]
            for student_id in list(students.keys())
            if self.id in list(students[student_id]["grades"].keys())
        ] #Checks if the students has the grade
        # and adds the grade to the list if the condition is checked

    def subject_average(self, subjects, students):
        """Calculates and returns the average grade for a subject"""
        subjects[self.id]["grades"] = self.all_grades(students)
        return sum(subjects[self.id]["grades"]) / len(
            subjects[self.id]["grades"])


class Classroom():
    """Represents a classroom containing students and subjects"""

    def __init__(self, classroom_id, classroom_students, classroom_subjects, classroom_name):
        """Initializes a classroom with ID, name, students and subjects"""
        self.id = classroom_id
        self.students = classroom_students
        self.subjects = classroom_subjects
        self.name = classroom_name

    def add_classroom(self, classrooms):
        """Adds a classroom with ID and name"""
        classrooms[self.id]["name"] = self.name

    def add_student(self, student_id, student_name, student_prename, students):
        """Adds a student in the dictionary students"""
        students[student_id] = {"name": student_name, "prename": student_prename,
                                  "classroom": self.name, "grades":{}}

    def delete_student(self, student_id, students):
        """Deletes a student from the dictionary students"""
        del students[student_id]

    def add_subject(self, subject_id, subject_name, subject_weight, subjects):
        """Adds a subject in the dictionary subjects"""
        subjects[subject_id] = {"name": subject_name, "weight": subject_weight}

    def delete_subject(self, subject_id, subjects):
        """Deletes a subject from the dictionary subjects"""
        del subjects[subject_id]

    def search_student(self, student_id_or_name, students):
        """Searches for a student in the dictionary students"""
        if isinstance(student_id_or_name, int):
            return students[student_id_or_name]
        return [students[student_id] for student_id in list(students.keys())
                if students[student_id]["name"] == student_id_or_name]
