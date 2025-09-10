def print_neg(l):
    for i in l:
        if i<0:
            print(i)
def list_ex():
    l=[]
    n= int(input("Enter number of elements: "))
    for i in range(n):
        k=int(input("enter number"))
        l.append(k)
    print_neg(l)
list_ex()