#Full name: Ahsan Mohammed
#Date: 4/16/2026
#Chapter number: C9  
#Assignment name: Working with Sets
#Description: Define 2 sets and then use various functions to manipulate said sets

set1 = set(["Jack", "Charlie", "Sawyer", "Kate", "Sayid", "Sun", "Desmond"])#set up initial set 1 -AM
set2 = set(["Hurley", "Jin", "Boone", "Jack", "Kate","Sawyer", "Juliet"])# set up the othe initial set-AM
print("initial print of unadulterated set")

for name in set1:#initial print of unadulterated set -AM
    print(name)#printing out the elements -AM
print()#extra space for easierto understand output -AM

print("initial print of unadulterated set number 2")
for name in set2:#initial print of unadulterated set number 2 -AM
    print(name)
print()#extra space for readability-AM
print("iterate over the values that occur in both sets")
for name in set1.intersection(set2):#iterate over the values that occur in both sets -AM
    print(name)#actually print the values we iterate over-AM
print()
print("iterate over all distinct values, effectively concatenating the sets and then redefining as a set to eliminate duplicates")
for name in set1.union(set2):#iterate over all distinct values, effectively concatenating the sets and then redefining as a set to eliminate duplicates -AM
    print(name)
print()
print("iterate over the values that show up in set 1 but not set 2")
for name in set1.difference(set2):#iterate over the values that show up in set 1 but not set 2-AM
    print(name)
print()
print("iterate over the values that show up in set 2 but not set 1")
for name in set2.difference(set1):#iterate over the values that show up in set 2 but not set 1 -AM
    print(name)
print()