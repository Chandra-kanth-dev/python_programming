def is_alphabet(a):
    if((ord(a)>=65 and ord(a)<=91) or(ord(a)>=97 and  ord(a)<=122)):
        
        return True
    else:
        return False
print(is_alphabet('a'))
