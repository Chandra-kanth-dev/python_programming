from collections import Counter
def minimize_string(s):
    d=Counter(s)
    res=""
    for i in d.keys():
        res=res+i+str(d[i])
    return res
s=((input("enter a string")))
print("minimized string",minimize_string(s))