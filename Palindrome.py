#This code is not working 13-Feb-2023
n=int(input("Enter something to check palindrome : "))
temp=n
while n!=0:
    pal=int(+n%10)
    print(pal)
    n=n/10
    print(n)
if temp==pal:
    print("The {} is a palindrome.".format(temp))
else:
    print("The {} is not a palindrome.".format(temp))
    