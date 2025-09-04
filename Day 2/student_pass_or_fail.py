#STUDENT DETAILS AND MARKS IN 3 SUBJECTS
def get_grade(marks):
    if marks>40:
        if marks>80:
            return "S grade"
        elif marks>=71 and marks<=80:
            return "A grade"
        elif marks>=51 and marks <=70:
            return "B grade"
        elif marks>40 and marks<=50:
            return "C grade"
    else:
        return "Fail"
s_name = input("enter name of student")
s_id = input("enter id of student")
marks= []
print("enter 3 sujects marks")
for i in range(0,3):
    print("enter marks of subject",i+1)
    marks.append(int(input()))
total = marks[0]+marks[1]+marks[2]
avg = round(total/3,2)

print("name is : ", s_name)
print("student id is " , s_id)
print("marks in 3 subjects are")
print(*marks)
print("total marks", total)
print("average marks", avg)
print("the grade of student is ",get_grade(avg))
