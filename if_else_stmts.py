def is_even_number(a):
    if(a%2==0):
        return True
    else:
        return False
num = int(input("enter a number"))
if(is_even_number(num)):
    print(num , "is even")
else:
    print(num, "is odd")