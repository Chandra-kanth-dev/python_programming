'''A 3-day tech workshop collected attendee registrations separately for each day. You are given three lists (day1, day2, day3) of email addresses — lists may contain duplicates (people registering multiple times) and email case may vary (Upper/Lower).

Write a Python program that:
Cleans each day's list (normalizes case, removes duplicates).
Prints the total number of unique attendees across all days.
Prints the list of attendees who attended all three days.
Prints the list of attendees who attended exactly one day.
Prints pairwise overlap counts (day1 & day2, day2 & day3, day1 & day3).
Produces a final report with counts and sorted lists for each of the above outputs.'''
 

l_day1=[]
l_day2=[]
l_day3=[]
n1=int(input("enter number of attendees on day 1"))
for i in range(n1):
    l_day1.append(input().lower())
n2=int(input("enter number of attendees on day 2"))
for i in range(n2):
    l_day2.append(input().lower())    
n3=int(input("enter number of attendees on day 3"))
for i in range(n3):
    l_day3.append(input().lower())
#cleaning
day1=(set(l_day1))
day2=(set(l_day2))
day3=(set(l_day3))
#printing total attendees
print("total unique attendees on day1",(day1),"total unique attendees on day2",day2,"total unique  attendees on day3",day3)
print("list of unique attendees on all 3 datys")
res1=(day1&day2&day3)
print(sorted(list(res1)))
print(len(res1))
print("list of unique 5attendees exactli one day")
res2=((day1-day2)-day3|(day2-day3)-day1|(day3-day1)-day2)
print(sorted(list(res2)))
print(len(res2))
print("day wise overalps day1&day2 etc")
res3=((day1&day2) ,(day2&day3),(day1&day3))
print(sorted(list(res3)))
print(len(res3))

