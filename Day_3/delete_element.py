
l=list(map(int,input().split()))
i=int(input("enter a number to perform deletion at that index"))
print("before delete",l)
l.pop(i)
print("after delete",l)
