def count_duplicates(l):
    c=0
    s=set()
    for i in l:
        if i in s:
            c+=1
        else:
            s.add(i)
    return c
l=list(map(int,input().split()))
print(count_duplicates(l))