import tkinter as tk
from tkinter import ttk

class GUI(tk.Tk):
    def __init__(self, model):
        super().__init__()
        self.index = -1

        self.title("Student Management System")
        self.geometry("600x400")
        self.studentmodel = model
        self.students = self.studentmodel.getStudents()

        self.create_table()
        self.btn = tk.Button(self, text="Delete", command=self.delete)
        self.btn.grid(row=2, column=2, pady=2)

    def create_table(self):
        columns = ["ID", "Name", "Age", "Gender", "Course", "Year"]
        self.tree = ttk.Treeview(self, columns=columns, show="headings")

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor="center")

        for student in self.students:
            self.tree.insert("", "end", values=(student.id, student.name, student.age, student.gender, student.course, student.year))

        self.tree.grid(row=0, column=0)

        # Bind the <<TreeviewSelect>> event to a callback function
        self.tree.bind("<<TreeviewSelect>>", self.clickEvent)

    def clickEvent(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            values = self.tree.item(selected_item, 'values')
            index = self.studentmodel.getIndex(values[0])
            self.index = index
            print(self.index)

    
    def delete(self):
        if self.index != -1:
            self.studentmodel.deleteStudent(self.index)
            self.refresh_table()
            self.index = -1

    def refresh_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        self.students = self.studentmodel.getStudents()

        for student in self.students:
            self.tree.insert("", "end", values=(student.id, student.name, student.age, student.gender, student.course, student.year))





