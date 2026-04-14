def count_vowels(string1):

    vowel_counts = dict()
    vowel_counts["a"]=0
    vowel_counts["e"]=0
    vowel_counts["i"]=0
    vowel_counts["o"]=0
    vowel_counts["u"]=0
    for letter in string1:
        letter=letter.lower()
        for vowel in vowel_counts:
            if vowel==letter:
                vowel_counts[vowel] += 1
    return vowel_counts

#testing it
"""
print(count_vowels(input()))
"""