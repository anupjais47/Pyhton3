num=int(input("Enter a number to revese : "))
rev=0
while num!=0:
    rev=rev*10+num%10
    num=num//10
# for num in range(-1,0):
#     print(num)
print(rev)