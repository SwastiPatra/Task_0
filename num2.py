Str = input("enter a string: ")
words = Str.split()
lower = []
upper = []
for char in Str:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)
sortedstring = ''.join(lower + upper)
print("\n arranging characters giving precedence to lowercase:")
print(sortedstring)