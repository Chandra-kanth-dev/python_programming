from collections import Counter
def print_unique_elements(l):
    d=Counter(l)
    return d
l=list(map(int,input().split()))
d=print_unique_elements(l)
for i,j in d.items():
    if j==1:
        print(i)
