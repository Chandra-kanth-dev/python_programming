

def is_prime(n):
    c=1
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            c+=1
    return  c==1

print(is_prime(int(input("enter a number"))))