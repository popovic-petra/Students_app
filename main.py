import random

class Course:
    def __init__(self, name, course_code):
        self.name = name
        self.course_code = course_code
        self.students = []
    def __str__(self):
        return "%s [%s]"%(self.name, self.course_code)
    def print(self):
        print("===============")
        print(self)
        print("===============")
        for i, student in enumerate(self.students):
            print(f"{i+1}. {student}")

class Student:
    def __init__(self, name, lastname, student_number):
        self.name = name
        self.lastname = lastname
        self.student_number = student_number
        self.classes = []
    def __str__(self):
        return "%s %s (%s)" %(self.name, self.lastname, self.student_number)
    def enroll(self, course):
        self.classes.append(course)
        course.students.append(self)

def main():

    students = [Student("Mario", "Mandic", "1234"),
                Student("Ana", "Ljubic", "2345"),
                Student("Petra", "Popovic", "3432"),
                Student("Ana", "Mikic", "3221")]
    
    courses = [Course("Programiranje 1", "S101"),
               Course("Baze podataka", "S202")]
    
    for student in students:
        student.enroll(random.choice(courses))

    for course in courses:
        course.print()

if __name__ == "__main__":
    main()