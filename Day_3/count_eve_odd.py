def count_even_odd(l):
    o=0
    e=0
    for i in l:
        if i%2==0:
            e+=1
        else:
            o+=1
    return (e,o)
l=list(map(int,input().split()))
print(count_even_odd(l))
e,o=count_even_odd(l)
print("even count",e)
print("odd count",o)