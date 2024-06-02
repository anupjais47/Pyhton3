n=int(input("Enter the length of the list : "))
list=[]
odd=[]
even=[]
print("Enter the numbers ")
for i in range(0,n):
    ele = int(input())
    list.append(ele)
for i in range(0,n):
    if list[i]%2==0:
        eve=list[i]
        even.append(eve)
    else:
        eve=list[i]
        odd.append(eve)
print("Even ",even)
print("Odd ",odd)