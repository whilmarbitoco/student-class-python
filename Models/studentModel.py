from student import Student

class studentModel:
    def __init__(self) -> None:
        self.studentList = [Student(1, "John Doe", 20, "Male", "BSIT", 2),
            Student(2, "Jane Doe", 22, "Female", "BSHM", 3),]

    def addStudent(self,student):
        self.studentList.append(student)

    def getStudents(self):
        return self.studentList
    
    def getStudent(self, name):
        if len(self.studentList) > 0:
            for student in self.studentList:
                if student.name == name:
                    return student
                else:
                    return -1
        else:
            return -1
    
    def getIndex(self, id):
        for index, student in enumerate(self.studentList):
            if int(student.id) == int(id):
                return index
        return -1


    def deleteStudent(self, index):
        self.studentList.pop(index)

    def editStudent(self, name, age, gender, course, year):
        index = self.getIndex(name)
        newStudent = Student(name, age, gender, course, year)
        self.studentList[index] = newStudent