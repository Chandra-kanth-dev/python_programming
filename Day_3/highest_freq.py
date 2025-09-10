from collections import Counter
def highest_freq(s):
    d=Counter(s)
    max_freq=0
    max_freq_val=0
    for i,j in d.items():
        if j>max_freq:
            max_freq_val=i
            max_freq=j
    return(max_freq_val,max_freq)
print(highest_freq(input("eneter a string")))