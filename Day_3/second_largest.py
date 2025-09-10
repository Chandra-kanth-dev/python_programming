def second_lar(li):
    m=float('-inf')
    sm=float('-inf')
    for i in li:
        if i>m:
            sm=m
            m=i
        if m>i and sm<i:
            sm=i
    if sm==float('-inf'):
        return "not found"
    return sm
l=list(map(int,input().split()))
print(second_lar(l))
    
    
    