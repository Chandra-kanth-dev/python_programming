def add_element(s,e):
    s.add(e)
def remove_element(s,e):
    s.remove(e)
def display(s):
    print(s)
def search(s,e):
    if e in s:
        return True
    return False
def union(s1,s2):
    return s1.union(s2)
def intersection(s1,s2):
    return s1.intersection(s2)
def difference(s1,s2):
    return s1.difference(s2)
def symmetric_difference(s1,s2):
    return s1.symmetric_difference(s2)
s1={1,2,3,4,5,6,7,8}
s2={5,6,7,8,9,10,11,12}
while(True):
    print("1.add element\n2.remove element\n3.search element\n4.display\n5.union\n6.intersection\n7.difference\n8.symmetric difference\n9.exit")
    choice=int(input("enter your choice"))
    if choice==1:
        e=int(input("enter an element to add"))
        add_element(s1,e)
        print("element added")
    elif choice==2:
        e=int(input("enter an element to remove"))
        remove_element(s1,e)
        print("element removed")
    elif choice==3:
        e=int(input("enter an element to search"))
        if search(s1,e):
            print("element found")
        else:
            print("element not found")
    elif choice==4:
        print("the elements are")
        display(s1)
    elif choice==5:
        print("union is",union(s1,s2))
    elif choice==6:
        print("intersection is",intersection(s1,s2))
    elif choice==7:
        print("difference is",difference(s1,s2))
    elif choice==8:
        print("symmetric difference is",symmetric_difference(s1,s2))
    elif choice==9:
        break
    else:
        print("enter a valid choice")
        