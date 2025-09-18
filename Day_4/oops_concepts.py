class Student:
    name=""
    roll_no=0
    marks=0
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
        
    def display(self):
        print("name",self.name)
        print("roll_no",self.roll_no)
        print("marks",self.marks)
jyothi = Student("jypthimurali","5ct",99)
jayanth=Student("veerabadram","5cs",76)
jyothi.display()
jayanth.display()
