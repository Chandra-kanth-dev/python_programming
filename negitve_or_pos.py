def is_negative(a):
    if(a<0):
        return True
    else:
        return False
num = int(input("enter a number"))
if(is_negative(num)):
    print(num , "is negative")
else:
    print(num , "is positive")