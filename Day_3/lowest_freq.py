from collections import Counter
def lowest_freq(s):
    d=Counter(s)
    min_freq=0
    min_freq_val=0
    for i,j in d.items():
        if j<min_freq:
            min_freq_val=i
            min_freq=j
    return(min_freq_val,min_freq)
print(lowest_freq(input("enter a string")))