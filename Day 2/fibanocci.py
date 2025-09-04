def fibanocci(n):
    if n<=1:
        return n
    else:
        return fibanocci(n-1)+fibanocci(n-2)
n=int(input("enter a number"))
for i in range(0,n):
    print(fibanocci(i),end = " ")
