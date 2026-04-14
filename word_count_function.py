def common_word_count(a, b):

    list_a = a.split(" ")
    list_b = b.split(" ")
    set_a = set(list_a)
    set_b = set(list_b)
    common_set = set_a.intersection(set_b)
    
    final_dict=dict()
    for common_word in common_set:
        final_dict[common_word] = 0
    for word in list_a+list_b:
        if word in common_set:
            final_dict[word] +=1
    
    return final_dict
#testing it below
"""
a = input()
b=input()
print(common_word_count(a,b))
"""




