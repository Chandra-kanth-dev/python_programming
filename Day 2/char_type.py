def char_type(c):
    if ((c>'A' and  c <'Z') or (c>'a' and c<'z')):
        return "alphabet"
    elif c in ['1','2','3','4','5','6','7','8','9','0']:
        return "number"
    else:
        return "special character"
a = (input("enter a character"))
print(char_type(a))
