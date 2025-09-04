

def is_prime(n):
    c=1
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            c+=1
    return  c==1

def prime_factors(n):
    for i in range(1,n):
        if is_prime(i) and n%i==0:
            print(i)
prime_factors(int(input("enterb a number")))