def GCD(n1,n2):
    while n1 != n2 :
      if n1>n2 :
        n1 -= n2
      else :
        n2-=n1
    return n1

def LCM(n1,n2):
  for i in range(1,n2):
    if n1%i == 0 and n2%i == 0 :
        lcm = i
    
    lcm = int(n1*n2/lcm)
    return lcm

n1=int(input("Enter the first numbers : "))
n2=int(input("Enter the second numbers : "))
result=GCD(n1,n2)
print(f"The GCD of {n1} and {n2} is ",end=" ")
print(result)
result=LCM(n1,n2)
print(f"The LCM of {n1} and {n2} is ",LCM(n1,n2))
# print(f"The LCM of {n1} and {n2} is ",result)
# print(result)
# print(f"The GCD of {n1} and {n2} is ")
