def count_vowels_cons(s):
    vowels=['A','a','E','e','I','i','O','o','U','u']
    vow_c=0
    cons_c=0
    for i in s:
        if i in vowels:
            vow_c+=1
    cons_c=len(s)-vow_c
    return(vow_c,cons_c)
s=input("enter a string")
res=(count_vowels_cons(s))
print("count of vowels",res[0],"count of consonanats",res[1])