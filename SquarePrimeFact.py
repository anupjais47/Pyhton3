import math
n=int(input("Enter a number : "))
print("Square Root ",int(math.sqrt(n)))
print("Square ",(n**2))
print("Factorial ",math.factorial(n))
flag=1
for i in range(2,n//2):
    if n%i==0:
        flag=0
        break
if flag==1:
    print(n," is a prime number.")
else:
    print(n," is not a prime number.")

