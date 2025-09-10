def tupl_operations(l):
    #print name who scored highest marks
    maximum_marks=0
    name=""
    print("name of student who scored maximum marks")
    for i in l:
        if i[2]>maximum_marks:
            name=i[1]
            maximum_marks=i[2]
    print(name,maximum_marks)
    print("students who scored above 75 maks")
    for i in l:
        if i[2]>=75:
            print(i[1],i[2])
    

l=[]
for i in range(5):
    n=(input("enter name"))
    roll = input("enter roll number")
    marks=int(input("enter marks"))
    l.append((roll,n,marks))
tupl_operations(l)
