def multiplication_or_sum(a,b):
    product = a*b
    if(product<=1000):
      return product
    else:
      return a+b
a= int(input("enter first number: "))
b= int(input("enter second number: "))
result=multiplication_or_sum(a,b)
print("The result is",result)
