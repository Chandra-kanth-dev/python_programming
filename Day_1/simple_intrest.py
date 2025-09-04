#CALCULATING SIMPLE INTREST AND TOTAL AMOUNT
principal_amt = int(input("enter principal amount"))
time = int(input("enter time in months"))
rate = int(input("enter the rate "))
s_i = (principal_amt*time*rate)//100
print("simple intrest is ", s_i)
print("total amount is ", principal_amt+s_i)