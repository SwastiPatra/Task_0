def outerFun(a,b):
     square = a**2
     def innerFun(a,b):
         return a+b
     add = innerFun(a,b)
     return add+5
a = int(input("enter value of a: " ))
b = int(input("enter value of b: "))
result = outerFun(a,b)
print(result)