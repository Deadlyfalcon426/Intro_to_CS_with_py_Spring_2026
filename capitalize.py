text = input()
char_before = ""
new_text = ""
for char in text:
    if char_before=="" or char_before == ".":
        new_text+=char.upper()
    else:
        new_text+=char.lower()
    if char != " ":
        char_before = char
print(new_text)