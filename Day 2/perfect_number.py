def perfect_number(n):
    res=0
    for i in range(1,n-1):
        if n%i==0:
            res+=i
    return res==n
n=int(input("enter a  number"))
for i in range(n):
    if perfect_number(i):
        print(i)