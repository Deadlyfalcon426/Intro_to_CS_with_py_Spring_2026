class Student:
    def __init__(self):
        self.name = ""
        self.id = ""
        self.department = ""
        self.program = ""
    def set_name(self, name):
        self.name = name
    def set_id_number(self, id):
        self.id = id
    def set_department(self, dep):
        self.department = dep
    def set_study_program(self, prog):
        self.program = prog
    def get_name(self):
        return self.name
    def get_id_number(self):
        return self.id
    def get_department(self):
        return self.department
    def get_study_program(self):
        return self.program
    
students = [0]*4

students[0] = Student()
students[0].set_name("Lilian Jones")
students[0].set_id_number("490242")
students[0].set_department("Humanities")
students[0].set_study_program("Bachelor's in English Literature")

students[1] = Student()
students[1].set_name("Frank Stalfrei")
students[1].set_id_number("784921")
students[1].set_department("Humanities")
students[1].set_study_program("Master's in North American History")

students[2] = Student()
students[2].set_name("Zheng Morsey")
students[2].set_id_number("012523")
students[2].set_department("Physics")
students[2].set_study_program("Bachelor's in Physics")

students[3] = Student()
students[3].set_name("Antonio Moretta")
students[3].set_id_number("472862")
students[3].set_department("Computer Science")
students[3].set_study_program("Master's in Distributed Computing")

for student in students:
    print(f"Name: {student.get_name()}")
    print(f"ID Number: {student.get_id_number()}")
    print(f"Department: {student.get_department()}")
    print(f"Study Program: {student.get_study_program()}")
    print()
    print()