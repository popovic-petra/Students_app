import random
from classes.course import Course
from classes.student import Student
from classes.student_generator import StudentGenerator

def main():

    gen = StudentGenerator()
    student = gen.get_n(20)

    courses = [Course("Programiranje 1", "S101"),
               Course("Baze podataka", "S202")]
    
    for student in student:
        student.enroll(random.choice(courses))

    for course in courses:
        course.print()

if __name__ == "__main__":
    main()