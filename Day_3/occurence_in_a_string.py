def count_print_occurences_of_a_character(s,ch):
    count=0
    l=[]
    for i in range(len(s)):
        if s[i]==ch:
            count+=1
            l.append(i)
    return count,l
s=input("enter a string")
ch=input("enter a character")
print(count_print_occurences_of_a_character(s,ch))
