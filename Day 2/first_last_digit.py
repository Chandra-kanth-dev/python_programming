def first_and_last(n):
    li=[]
    k=n%10
    while(n>10):
        n=n//10
    li.append(n)
    li.append(k)
    return li
v=first_and_last(int(input("enter a number ")))
print(v)
print("sum of first and last ", v[0]+v[1])