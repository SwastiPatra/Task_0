
#program to print all the prime numbers in a given interval
lower = int(input("Enter the lower range: "))
upper = int(input("Enter the upper range: "))
for n in range(lower,upper+1):
    if(n > 1):
        for i in range(2,n):
          if(n % i) == 0:
              break
        else:
          print(n)
#now to check a given number is prime or not
a= int(input("Enter a number: "))
j=1
if(a > 1):
  for j in range(2,a):
      if(a % j) == 0:
          print(a,"is not a prime number")
          break
  else:
          print(a,"is prime")
else:
      print(a,"is not a prime number")   
