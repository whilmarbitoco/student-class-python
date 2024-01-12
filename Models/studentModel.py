from student import Student

class studentModel:
    def __init__(self) -> None:
        self.studentList = []

    def add(self,student):
        self.studentList.append(student)

    def display(self):
        if len(self.studentList) > 0:
            for student in self.studentList:
                print(f"Name: {student.name}")
                print(f"Age: {student.age}")
                print(f"Gender: {student.gender}")
                print(f"Course: {student.course}")
                print(f"Year: {student.year}")
        else:
            print("No Current Students")
    
    def getIndex(self, name):
        if len(self.studentList) > 0:
            for student in self.studentList:
                if student.name == name:
                    return self.studentList.index(student.name)
        else:
            return -1

    def delete(self, index):
        self.studentList.pop(index)

    def edit(self, name, age, gender, course, year):
        index = self.getIndex(name)
        newStudent = Student(name, age, gender, course, year)
        self.studentList[index] = newStudent