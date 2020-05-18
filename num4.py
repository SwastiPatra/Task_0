str=input("enter a string\n")
index = 0
for index in range(len(str)):
    if index % 2 == 0:
        print(str[index],end='')
