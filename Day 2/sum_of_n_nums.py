def sum_of_n_natural_nums(n):
    i=1
    res=0
    while(i<=n):
        res+=i
        i+=1
    return res
print(sum_of_n_natural_nums(int(input("enter a number: "))))