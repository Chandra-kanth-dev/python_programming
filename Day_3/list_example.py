#adding elements to list and printing them
def list_ex():
    l=[]
    n= int(input("Enter number of elements: "))
    for i in range(n):
        k=int(input("enter number"))
        l.append(k)
    print(l)
list_ex()