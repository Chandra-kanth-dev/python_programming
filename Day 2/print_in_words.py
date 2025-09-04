def print_in_words(n):
    d={
        1:"one",
        2:"two",
        3:"three",
        4:"four",
        5:"five",
        6:"six",
        7:"seven",
        8:"eight",
        9:"nine",
        0:"zero"
    }
    res=[]
    while(n>0):
        res.append(d[n%10])
        n=n//10
    return ' '.join(res[: : -1])
print(print_in_words(1234))