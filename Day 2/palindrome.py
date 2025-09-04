def is_palindrome(n):
    k=n
    res=0
    for i in range(len(str(n))):
        res=res*10
        res=res+(n%10)
        n//=10
    return k==res
a = int(input("enter a number"))
if is_palindrome(a):
    print("yes its a palindrome")
else:
    print("no its not a palindrome")