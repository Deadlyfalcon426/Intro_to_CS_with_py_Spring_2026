"""
fav_colors={'fav1':'red', 'fav2':'green', 'fav3':'blue'}
print(fav_colors)

print(fav_colors.get("fav5", "color not found"))

print(fav_colors.keys())



fav_colors["7"] = "purple"
print(fav_colors.pop("7", "keyNotFound"))



#fav_colors.clear()
print(fav_colors)


print(fav_colors.popitem())
print(fav_colors)


print(fav_colors.get("fav5", "color not found"))

"""
"""
dictionary_1 = dict()
dictionary_1["entry"] = 1
dictionary_2 = {'key':'value'}
dict3 = dictionary_1 | dictionary_2
print(dict3)
"""
myset = set([1,3,4,7,9])
print(myset)
print(len(myset))

set2 = set([1,8,4,7,99999])
print(myset.intersection(set2))
print(set2)
print(myset.union(set2))

print(myset.symmetric_difference(set2))