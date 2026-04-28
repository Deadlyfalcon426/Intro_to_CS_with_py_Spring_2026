names = []
with open ('popular_names.txt', 'r') as popnames:
    for line in popnames:
        names.append(line.strip())
qname = input("Enter a name: ")
if qname in names:
    print("That was a popular name between 2000 and 2009.")
else:
    print("That was not a popular name between 2000 and 2009.")