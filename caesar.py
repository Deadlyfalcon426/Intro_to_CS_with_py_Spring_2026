key = 1
input_list = list(input())
output_list = ["0"] *len(input_list)
x=0
for letter in input_list:
    output_list[x] = chr(ord(letter)+key)
    x = x+1
print("".join(output_list))