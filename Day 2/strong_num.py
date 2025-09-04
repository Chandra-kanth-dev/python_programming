def fact(n):
    a=1
    while(n>0):
        a*=n
        n-=1
    return a
def strong(n):
    k=n
    res=0
    for i in range(len(str(n))):
        res=res+fact(n%10)
        n//=10
    return res
n = int(input("enter a number"))
print("the strong numbers from 1 to n are")
for i in range(n+1):
    if i==strong(i):
        print(i)
        