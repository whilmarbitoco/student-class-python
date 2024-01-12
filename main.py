from student import Student
from Controllers.studentController import studentController

def main():
    studentcontroller = studentController()
    while True:
        print("[1] ADD \n[2] EDIT \n[3] DELETE \n[4] DISPLAY \n[5] EXIT")
        prompt = int(input("[choice]> "))
        
        if prompt == 1:
            studentcontroller.create()
        elif prompt == 2:
            pass
        elif prompt == 3:
            pass
        elif prompt == 4:
            studentcontroller.show()
        elif prompt == 5:
            break
        else:
            print("Invalid Option")



if __name__ == "__main__":
    main()