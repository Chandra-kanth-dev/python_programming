def is_palindrome(n):
    k=n
    res=0
    for i in range(len(str(n))):
        res=res*10
        res=res+(n%10)
        n//=10
    return k==res

n = int(input("enter a number"))
for i in range(n+1):
    if is_palindrome(i):
        print(i)