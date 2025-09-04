def calc_bill(bill):
    res=0
    a=[3.80,4.20,5.10,6.30,7.50]
    while(bill>0):
        if bill>1 and bill<=50:
            res+=(a[0]*(bill-50))
            bill=bill-50
        elif bill>=51 and bill<=100:
            res+=(a[1]*(bill-50))
            bill=bill-50
        elif bill>=101 and bill<=200:
            res+=(a[2]*(bill-100))
            bill=bill-100
        elif bill>=201 and bill<=300:
            res+=(a[3]*(bill-100))
            bill=bill-100
        else:
            res+=bill*a[4]
            
            

#printing customer details and bill 
c_num = int(input("enter customer id/number "))
c_name= input("enter customer name ")
prev_reading = int(input("enter previous month readin "))
curr_reading = int(input("enter current month reading "))
total_units = curr_reading-prev_reading
bill_amt = calc_bill(total_units)
print("customer name" , c_name,"customer id" , c_num, "total amount to pay" , bill_amt)