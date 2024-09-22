import random
from classes.course import Course
from classes.student import Student

def main():

    students = [Student("Mario", "Mandic", "1234"),
                Student("Ana", "Ljubic", "2345"),
                Student("Luka", "Lukic", "3432"),
                Student("Mara", "Mandic", "3432"),
                Student("Grgo", "Jovanic", "3432"),
                Student("Ana", "Mikic", "3221")]
    
    courses = [Course("Programiranje 1", "S101"),
               Course("Baze podataka", "S202")]
    
    for student in students:
        student.enroll(random.choice(courses))

    for course in courses:
        course.print()

if __name__ == "__main__":
    main()