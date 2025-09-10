def length_of_string(s):
    count=0
    for i in s:
        count+=1
    return count
s=(input("enter a string"))
print("the length of string is ",length_of_string(s))
t=input("enter another string")
if s==t:
    print("both strings are equal")
else:
    print("not equal")
print("concatenation of two styrings is",s+t)