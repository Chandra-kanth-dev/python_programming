#printing customer details and bill 
c_num = int(input("enter customer id/number "))
c_name= input("enter customer name ")
prev_reading = int(input("enter previous month readin "))
curr_reading = int(input("enetr current month reading "))
amt_per_unit = float(input("enter amount per unit in rupees "))

total_units = curr_reading-prev_reading
bill_amt = round(amt_per_unit*total_units,2)
print("customer name" , c_name,"customer id" , c_num, "total amount to pay" , bill_amt)