#Full name: Ahsan Mohammed
#Date: 2/17/26
#Chapter number: 4
#Assignment name:  C4 (In-Class Exercise) Python Programming Assignment - Nested Looping
#Description: The program prints out my full name in rows and columns, both of which are decided by the user.
initials_and_hyphen = "AM-" #save the base output as a variable to make it easy to read
rows = int(input("How many rows? "))#ask how many rows
columns = int(input("How many columns? "))#ask how many columns
for i in range(rows):#set up first loop, rows
    for j in range(columns):#set up second loop, columns
        print(initials_and_hyphen, end="")#print, use end='' to prevent newline
    print()#go to next row