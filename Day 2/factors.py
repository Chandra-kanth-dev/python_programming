def print_factors(n):
    for i in range(1,n):
        if n%i==0:
            print(i)
print_factors(int(input("enterb a number")))