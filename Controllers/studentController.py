from Models.studentModel import studentModel
from student import Student

class studentController:
    def __init__(self, model, view):
        self.studentmodel = model
        self.view = view

    def getGender(self, choice):
        if choice == 1:
            return "Male"
        elif choice == 2:
            return "Female"
    
    def getYearLevel(self, choice):
        if 1 <= choice or choice <= 4:
            return f"{choice}st year"
        else:
            return "Invalid"
        
    def getCourse(self, choice):
        courses = ["BSIT", "BSHM", "BSBA", "BSED"]
        if choice > len(courses):
            return "Invalid"
        else:
            return courses[choice-1]
        
    def create(self):
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        while True:
            gender = self.getGender(int(input("Enter your gender [1]Male [2]Female: ")))
            if gender == "Male" or gender == "Female":
                break
        while True:
            year = self.getYearLevel(int(input("Enter your year 1 - 4: ")))
            if year != "Invalid":
                break

        while True:
            print("[1]BSIT [2]BSHM [3]BSBA [4]BSED")
            course = self.getCourse(int(input("Enter your course: ")))
            if course != "Invalid":
                break

        newStudent = Student(name, age, gender, course, year)
        self.studentmodel.addSt(newStudent)


    def show(self):
        self.studentmodel.display()
    
    def delete(self):
        name = input("Enter name you wanna delete: ")
        self.studentmodel.delete(name)
        print("Successfuly Deleted.")
    
    def edit(self):
        name = input("Enter your name you wanna edit: ")
        if self.studentmodel.getIndex(name) == -1:
            print("No records Found")
    
        else:
            age = int(input("Enter your age: "))
            while True:
                gender = self.getGender(int(input("Enter your gender [1]Male [2]Female: ")))
                if gender == "Male" or gender == "Female":
                    break
            while True:
                year = self.getYearLevel(int(input("Enter your year 1 - 4: ")))
                if year != "Invalid":
                    break

            while True:
                print("[1]BSIT [2]BSHM [3]BSBA [4]BSED")
                course = self.getCourse(int(input("Enter your course: ")))
                if course != "Invalid":
                    break

            editStudent = Student(name, age, gender, course, year)
            self.studentmodel.edit(editStudent)

    def run(self):
        self.view.mainloop()