def remove_dubs(l):
    l=sorted(l)
    i=0
    j=0
    for j in range(1,len(l)):
        if j>0 and l[j]!=l[j-1]:
            i+=1
            l[i]=l[j]
    return l[0:i+1]
        


l=list(map(int,input().split()))
print(remove_dubs(l))