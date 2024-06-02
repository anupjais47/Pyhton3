n=int(input("Enter a number to check Armstrong : "))
temp=n
arm=0
while n!=0:
    m=int(n%10)
    # print(m)
    arm=int(arm+(m**3))
    # print(arm)
    n=int(n/10)
    # print(n)
if temp==arm:
    print("The entered number is an Armstrong.")
else:
    print("The entered number is not an Armstrong.")
