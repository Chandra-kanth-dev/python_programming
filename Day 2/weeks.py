def get_day(num):
    if num ==1:
        return "sunday"
    elif num==2:
        return "monday"
    elif num==3:
        return "tuesday"
    elif num==4:
        return "wednesday"
    elif num==5:
        return "thursday"
    elif num==6:
        return "friday"
    elif num==7:
        return "saturday"
    else:
        return "iunvalid day"
day = int(input("enetr the number of the day"))
print(get_day(day))