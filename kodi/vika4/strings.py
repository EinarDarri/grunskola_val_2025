string = input().strip()

print(string)
print("the string in all lower case", string.lower())
print("the string in all upper case", string.upper())
print("the length of the string", len(string))
print("the fyrst character of the string", string[0])
"Appelsína"
print("the string in reverse"[::-1], string[::-1])

print("is the string a digit", string.isdigit())
print("is the string all lower case", string.islower())
print("is the string all upper case", string.isupper())

new_string = ""

for staf in string:
    if len(new_string) == 0:
        new_string = new_string + staf
    elif new_string[-1] != staf:
        new_string = new_string + staf

print(new_string)

for i in range(6):
    print(i)
