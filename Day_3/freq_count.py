from collections import Counter
def count_freq(l):
    return Counter(l)
    #d={}
    #for i in l:
        #if i in d.keys():
           # d[i]+=1
        #else:
           # d[i]=1
    #return d
l=list(map(int,input().split()))
d=count_freq(l)
for i,j in d.items():
    print(i,"----->",j)
    