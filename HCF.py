def GCD(n1, n2):
    while n1 != n2 :
    if n1 > n2 :
      n1 -= n2
    else:
      n2 -= n1

    return n1
    # i=0
    # while m[i]%m[i+1]!=0:
    #     div=int(m[i]/m[i+1])
    #     m[i]=m[i+1]
    #     m[i+1]=m[i+2]

        # if m[i]%m[i+1]==0:
        #     return m[i]
        # else:
        #     m[i]=m[i+1]
    # return m[i]
# n=[2]
# n={}
# print("Enter a two numbers to find HCF : ")
n1=int(input("Enter the first numbers to find HCF : "))
n2=int(input("Enter the second numbers to find HCF : "))
# for i in range(4):
#     num=int(input())
#     n.append(num)

result=GCD(n1,n2)
print(n1)
print(result)
