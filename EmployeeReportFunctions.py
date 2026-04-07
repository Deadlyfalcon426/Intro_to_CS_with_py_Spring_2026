#Full name: Ahsan Mohammed
#Date: 3-3-26
#Chapter number: 5
#Assignment name: Lab Exam #4 – Employee System Using Functions
#Description: produce the report
def calculateBonus(salary, comm):
    return salary * comm
def inputData():
    employee_data = {
    }
    for x in range (3):
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        salary = int(input("Enter your salary: "))
        comm = float(input("Enter your commission percent: "))
        bonus = calculateBonus(salary, comm)
        employee_data[x] = [first_name, last_name, salary, comm, bonus]
    return employee_data
def reportHeader(employee_data):
    print("Employee System Report Functions")
    print()
    print()
    columns = ["First Name", "Last Name", "Salary", "Commission", "Bonus"]
    for column in columns:
        print(f"{column}\t\t", end='')
    print()
    for column in columns:
        for char in column:
            print("-", end='')
        print("\t\t", end='')
    print()
    #here is where the data is printed
    for person in employee_data:
        if person == 0:
            print(f"{employee_data[person][0]}\t\t\t{employee_data[person][1]}\t\t\t${employee_data[person][2]:.2f}\t{employee_data[person][3]}\t\t\t${employee_data[person][4]:.2f}")
        else:
            print(
                f"{employee_data[person][0]}\t\t\t{employee_data[person][1]}\t\t${employee_data[person][2]:.2f}\t{employee_data[person][3]}\t\t\t${employee_data[person][4]:.2f}")
def main():
    reportHeader(inputData())
main()