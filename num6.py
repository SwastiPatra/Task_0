#To print the fibonacci series
def fibo(n):
    if (n <= 1):
        return n
    else:
        return(fibo(n-1)+fibo(n-2))
terms = int(input("Enter no. of terms: "))        
if terms <= 0:
    print("Enter a positive number: ")
else:
    print("Fibonacci sequence: ")
    for i in range(terms):
        print(fibo(i))     
#To check if a input number is fibonacci or not
import math
def check(a):
    s = int(math.sqrt(a))
    return s*s == a
def isfibo(x):
    return check(5*x*x + 4) or check(5*x*x - 4)
x = int(input("Enter a number: "))
if isfibo(x):
    print(x,"is a fibonacci number")
else:
    print(x,"is not a fibonacci number")