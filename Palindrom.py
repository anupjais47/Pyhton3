num=int(input("Enter a number to check Palindrom : "))
temp1=num
temp=num

pal=True
rev=0
while temp!=0:
    rev=rev*10+temp%10
    temp=temp//10

while num!=0:
    if rev%10 != num%10:
        pal=False
        print(f"{num} is not a palindrome.")
        break
    num=num//10
    rev=rev//10

if pal==True:
    print(f"{temp1} is a palindrome.")