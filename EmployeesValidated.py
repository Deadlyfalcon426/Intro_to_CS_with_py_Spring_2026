#Full name: Ahsan Mohammed
#Date: 4-9-26
#Chapter number: 8
#Assignment name: Lab Exam #8 – Employee System - Validating Data
#Description: produce the report, however all data must be validated for proper format
def calculateBonus(salary, comm):
    return salary * comm


def validate(first = None, last = None, salary=None, comm=None):#use None so if i dont put in one then it still works -AM
    if first != None:
        if (first.isupper() and first.isalpha())==False: # check if both conditions filled -AM
            return False
        else:
            return True      
    elif last != None:
        if (last.islower() and last.isalpha())==False: # check if both conditions filled -AM
            return False
        else:
            return True  
    elif salary!=None: # check if salary works -AM
        try:#use try instead of usual -AM
            int(salary)
            return True
        except:
            return False  
    elif comm != None:
        try:
            float(comm)#using try again except we actually need it this time -AM
            return True
        except:
            return False  


def inputData():
    employee_data = {
    }
    error_message = "\nYou messed up something. Try again.\nStart from the beginning of the entry.\nFor example, if you were writing the first name, \nstart from that person's first name, not from the beginning of the list\n"
    for x in range (3):
        all_checks_passed=False
        while not all_checks_passed:
            first_name = input("Enter your first name: ").strip()
            if not (all_checks_passed:=validate(first=first_name)):#check if validated -AM
                print(error_message)#print fail message if wrong -AM
                continue#skip rest of while loop -AM

            last_name = input("Enter your last name: ").strip()
            if not (all_checks_passed:=validate(last=last_name)):
                print(error_message)
                continue

            salary = input("Enter your salary: ").strip()
            if not (all_checks_passed:=validate(salary=salary)):
                print(error_message)
                continue
            salary=int(salary)#do afterwards incase of fail -AM

            comm = input("Enter your commission percent: ").strip()
            if not (all_checks_passed:=validate(comm=comm)):
                print(error_message)
                continue
            comm = float(comm)

            bonus = calculateBonus(salary, comm)
        employee_data[x] = [first_name, last_name, salary, comm, bonus]
    return employee_data


def reportHeader(employee_data):
    with open('employeereport.txt','w') as output_file:
        output_file.write("Employee System Report Functions\n")
        output_file.write("\n")
        output_file.write("\n")
        columns = ["First Name", "Last Name", "Salary", "Commission", "Bonus"]
        for column in columns:
            output_file.write(f"{column}\t\t")####
        output_file.write("\n")
        for column in columns:
            for char in column:
                output_file.write("-")###
            output_file.write("\t\t")####
        output_file.write("\n")
        #here is where the data is printed -AM
        for person in employee_data:
            if person == 0:
                output_file.write(f"{employee_data[person][0]}\t\t\t{employee_data[person][1]}\t\t\t${employee_data[person][2]:.2f}\t{employee_data[person][3]}\t\t\t${employee_data[person][4]:.2f}\n")
            else:
                output_file.write(f"{employee_data[person][0]}\t\t\t{employee_data[person][1]}\t\t${employee_data[person][2]:.2f}\t{employee_data[person][3]}\t\t\t${employee_data[person][4]:.2f}\n")


def main():
    reportHeader(inputData())
main()