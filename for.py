#Full name: Ahsan Mohammed
#Date: 2/17/26
#Chapter number: 4
#Assignment name:  C4 (In-Class Exercise) Python Programming Assignment - For Loop
#Description: The program prints out my full name as many times as the user requests.
my_name = "Ahsan Mohammed"#my name is a variable to make it easy to type and to make code easier to read
counter = int(input("How many times would you like my full name to be printed? "))#asks user how many times they want my name to print
for x in range(counter):
    print(my_name)#print name