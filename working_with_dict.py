dict1={#set up initial dictionary, 2d dictionary
    1:{"Fn" : "John", "Ln" : "Smith", "Salary" : 40000},#i made each entry in the dictionary given by a key -AM
    2:{"Fn" : "Jalen", "Ln" : "Brunson", "Salary" : 30000}, #(rest of explanation)which is just their point in the order, -AM
    3:{"Fn" : "Rui", "Ln" : "Hachimura", "Salary" : 90000}#(rest of explanation)and within it theres another dictionary, a nested/2d dictionary -AM
}

for key in dict1.keys():#begin printing
    print(f"Fn{key}: {dict1[key]["Fn"]}")#we call the key for the first part, so we get the numbers like Fn1 -AM
    print(f"Ln{key}: {dict1[key]["Ln"]}")#(rest of explanation)then for the next part we call the dictionary key -AM
    print(f"Salary{key}: ${dict1[key]["Salary"]}")#on this line i added $ since salary -AM

print()#for space between steps, clear reading -AM

#step 2
dict1[1]["Fn"] = "JohnS"#just add it on manually by accessing the value from nested dict -AM
dict1[2]["Fn"], dict1[3]["Fn"] = "JalenM", "RuiA"#assigned other 2, used multiple assigment for fun -AM

for key in dict1.keys():#print them out again
    print(f"Fn{key}: {dict1[key]["Fn"]}")
    print(f"Ln{key}: {dict1[key]["Ln"]}")
    print(f"Salary{key}: ${dict1[key]["Salary"]}")#put the dollar sign here cause salary