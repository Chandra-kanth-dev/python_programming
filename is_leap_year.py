def is_leap_year(num):
    if(num%4==0 ):
        if(num%100==0) and num%400==0:
            return True
        else:
            False
    else:
        return False
year = int(input("enter a year"))
if(is_leap_year(year)):
    print("yes its leap year")
else:
    print("no !!!! not a leap year")