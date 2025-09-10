def count_types_of_chars(s):
    alphas =0
    digits=0
    specials =0
    for i in s:
        if i in "0123456789":
            digits+=1
        elif ((ord(i)>=65 and ord(i)<=91 )or (ord(i)>=97 and ord(i)<=123)):
            alphas+=1
        else:
            specials+=1
    return alphas,digits,specials
s=input("enter a string")
res=count_types_of_chars(s)
print("the alphabets count is",res[0],"digits count is",res[1],"special characters count is",res[2])