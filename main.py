from Views.views import GUI
from Models.studentModel import studentModel
from Controllers.studentController import studentController


def main():
    model = studentModel()
    view = GUI(model)
    controller = studentController(model, view)
    controller.run()
    

if __name__ == "__main__":
    main()