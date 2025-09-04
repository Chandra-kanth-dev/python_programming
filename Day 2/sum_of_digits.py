def sum_of_digits(n):
    res=0
    for i in range(len(str(n))):
        res=res+(n%10)
        n//=10
    return res
print(sum_of_digits(int(input("enter a number"))))