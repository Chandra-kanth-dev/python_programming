def add_product(l,product):
    l.append(product)
def remove_product(l,product):
    l.remove(product)

def display(l):
    print(l)
def total(l):
    return len(l)
l=[]
while(True):
    print("1.add product\n2.remove product\n3.search product\n4.display\n5.total number of products\n6.sort7.clear\n8.exit")
    choice = int(input("enter your choice"))
    if choice==1:
        product = (input("enetr a product"))
        add_product(l,product)
        print("product added")
    elif choice==2:
        product=(input("enter a product to removve"))
        remove_product(l,product)
        print("product removed")
    elif choice==3:
        product=(input("enter a product to search"))
        if product not in l:
            print("product not found")
        else:
            print("product found at index",l.index(product))
    elif choice==4:
        print("the products are")
        display(l)
    elif choice==5:
        print(total(l))
    elif choice==6:
        l.sort()
        print("sorted")
    elif choice==7:
        
        l.clear()
        print("cleared")
    elif choice==8:
        break
    else:
        print("enetr a valid choice")