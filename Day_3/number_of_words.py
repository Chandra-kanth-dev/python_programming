def count_words(s):
    if not s:
        return 0
    c=1
    for i in s:
        if i==" ":
            c+=1
    return c
s=input("enter a astring")
print(count_words(s))