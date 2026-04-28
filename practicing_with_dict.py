dict1= {#step1
    "Employee1_fn" : "John",
    "Employee1_ln" : "Smith",
    "Employee1_salary" : "40000",
    "Employee2_fn" : "Rui",
    "Employee2_ln" : "Hachimura",
    "Employee2_salary" : "90000",
    "Employee3_fn" : "Derrick",
    "Employee3_ln" : "White",
    "Employee3_salary" : "70000"
}
print()#spacing -AM

print(f"Employee1_fn: {dict1["Employee1_fn"]}")#step2
print(f"Employee1_ln: {dict1["Employee1_ln"]}")
print(f"Employee1_salary: {dict1["Employee1_salary"]}")
print(f"Employee2_fn: {dict1["Employee2_fn"]}")
print(f"Employee2_ln: {dict1["Employee2_ln"]}")
print(f"Employee2_salary: {dict1["Employee2_salary"]}")
print(f"Employee3_fn: {dict1["Employee3_fn"]}")
print(f"Employee3_ln: {dict1["Employee3_ln"]}")
print(f"Employee3_salary: {dict1["Employee3_salary"]}")
print()#spacing -AM

dict1["Employee1_fn"] = "JohnS"#step 3
dict1["Employee2_fn"] = "RuiA"
dict1["Employee3_fn"] = "DerrickR"
print()#spacing -AM

print(f"Employee1_fn: {dict1["Employee1_fn"]}")#print out each employee info
print(f"Employee1_ln: {dict1["Employee1_ln"]}")
print(f"Employee1_salary: {dict1["Employee1_salary"]}")
print(f"Employee2_fn: {dict1["Employee2_fn"]}")
print(f"Employee2_ln: {dict1["Employee2_ln"]}")
print(f"Employee2_salary: {dict1["Employee2_salary"]}")
print(f"Employee3_fn: {dict1["Employee3_fn"]}")
print(f"Employee3_ln: {dict1["Employee3_ln"]}")
print(f"Employee3_salary: {dict1["Employee3_salary"]}")
print()#spacing -AM

dict1["Employee1_email"] = "John_S_Smith@hotmail.com"#add employee 1 email
dict1.pop("Employee1_salary")#remove employee 1 salary
print()#spacing -AM

print(f"Employee1_fn: {dict1["Employee1_fn"]}")#print employee 1 info
print(f"Employee1_ln: {dict1["Employee1_ln"]}")
print(f"Employee1_email: {dict1["Employee1_email"]}")
print()#spacing -AM

for key in dict1.keys():#print all keys
    print(key)
print()#spacing -AM

for key in dict1.keys():#print all values
    print(dict1[key])

print()#spacing -AM
for key in dict1.keys():#print all key-value pairs
    print(f"{key} : {dict1[key]}")
