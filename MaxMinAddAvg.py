list=[]
n=int(input("Enter the range of  elements : "))
print("Enter the numbers : ")
for i in range(0, n):
    ele = int(input())
    list.append(ele)

print("List is ")
print(list)

print("The Max in the list")
print(max(list))

print("The Sum in the list")
print(sum(list))

print("The Average  in the list")
print(int((sum(list))/n))

print("The  Min in the list")
print(min(list))
# print("The MIN in the list")
# print(min)