from Models.studentModel import studentModel
from student import Student

class studentController:
    def __init__(self):
        self.stuentmodel = studentModel()

    def getGender(self, choice):
        if choice == 1:
            return "Male"
        elif choice == 2:
            return "Female"
    
    def getYearLevel(self, choice):
        if 1 <= choice <= 4:
            return f"{choice}st year"
        else:
            return "Invalid"

        
    def create(self):
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        while True:
            gender = self.getGender(int(input("Enter your gender [1]Male [2]Female: ")))
            if gender == "Male" or gender == "Female":
                break
        while True:
            year = int(input("Enter your year 1 - 4: "))
            if year != "Invalid":
                break

        course = input("Enter your year: ")
        newStudent = Student(name, age, gender, course, year)
        self.stuentmodel.add(newStudent)


    def show(self):
        self.stuentmodel.display()