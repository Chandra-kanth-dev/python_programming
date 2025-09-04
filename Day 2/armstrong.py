def pal(n):
    res=0
    for i in range(len(str(n))):
        res=res+(n%10)**3
        n//=10
    return res
n = int(input("enetr a number"))
if n==pal(n):
    print("yes armstrong")
else:
    print("nope")