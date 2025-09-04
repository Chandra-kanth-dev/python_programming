def fact(n):
    a=1
    while(n>0):
        a*=n
        n-=1
    return a
print(fact(int(input("enetr a number"))))