<<<<<<< HEAD

from classes.student import Student
=======
from student import Student
>>>>>>> master
import random

class StudentGenerator(object):

    NAMES = ["Petra", "Helena", "Katarina", "Rozalija", "Lucija", "Deni"]
    LNAMES = ["Popovic", "Orsolic", "Suljug", "Zivkovic", "Sebelic", "Vukajlovic"]

    def __init__(self):
        pass
    def get_n(self, n):
        """vrati n broj studenata iz liste"""
        students = []
        for i in range(n):
            name = random.choice(self.NAMES)
            lname = random.choice(self.LNAMES)
            number = random.randint(1000, 3000)
            students.append(Student(name, lname, number))
        return students
    
if __name__ == "__main__":
        gen = StudentGenerator()
        students = gen.get_n(10)

        for i in students:
            print(i)