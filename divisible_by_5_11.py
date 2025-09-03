def is_divisible_by_5_and_11(num):
    if(num%5==0 and num%11==0):
        return True
    else:
        return False
a=int(input("enter a number"))
if is_divisible_by_5_and_11(a):
    print("yes its divisible")
else:
    print("no its not divisible")
    