#Full name: Ahsan Mohammed
#Date: 4/28/2026
#Chapter number: C10
#Assignment name: Practice with Classes and Objects
#Description: Create a class to hold employee object
class Employee:

    def __init__(self):#initialize object -AM
        return
    def set_fn(self, fn):#make mutator functions -AM
        self.__fn = fn
    def set_ln(self, ln):
        self.__ln = ln
    def set_hiredate(self, date):
        self.__hiredate =date
    def set_department(self, dep):
        self.__department=dep
    def set_salary(self, sal):
        self.__salary = sal

    def get_fn(self):#make accessor functions -AM
        return self.__fn
    def get_ln(self):
        return self.__ln
    def get_hiredate(self):
        return self.__hiredate
    def get_department(self):
        return self.__department
    def get_salary(self):
        return self.__salary
    
def main():
    employees = [None]*2#set up employee list -AM
    employees[0] = Employee()#initialize and fill out first employee -AM
    employees[0].set_fn("John")
    employees[0].set_ln("Smith")
    employees[0].set_hiredate("3/5/24")
    employees[0].set_department("IT        ")#over here this is for spacing -AM
    employees[0].set_salary("125,000")

    employees[1] = Employee()#initialize and fill out second employee -AM
    employees[1].set_fn("James")
    employees[1].set_ln("Gordon")
    employees[1].set_hiredate("4/5/21")
    employees[1].set_department("Marketing")
    employees[1].set_salary("165,000")

    headers = ["First Name", "Last Name", "Hire Date", "Department", "Salary"]#list to store the headers -AM
    for header in headers:
        print(header, end='\t')
    print()#formatting

    spacing = "First Name      Last Name       Hire Date       Department      Salary "
    for chr in spacing:
        print("_", end='')#the line seperating column headers from data -AM
    print()

    for guy in employees:#next line prints them out, used 'guy' so i dont have to write much -AM
        print(f"{guy.get_fn()}\t\t{guy.get_ln()}\t\t{guy.get_hiredate()}\t\t{guy.get_department()}\t{guy.get_salary()}")


main()
