result=[]
print("Enter the obtained marks : ")
for i in range(0, 5):
    ele = int(input())
    result.append(ele)
for i in range(0,5):
    if(result[i]<40):
        print("You are fail")
        break
agr=(sum(result))/5

if(agr>75):
    print("You are awarded by distinctioin.")
elif(agr>=60 and agr<=75):
    print("You are awarded by First Division.")
elif(agr>=50 and agr<=60):
    print("You are awarded by Second Division.")
else:
    print("You are awarded by Third Division.")
print(agr)