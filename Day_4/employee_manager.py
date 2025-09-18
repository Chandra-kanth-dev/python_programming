class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print("name",self.name)
        print("salary ",self.salary)
class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department

    def display(self):

        super().display()
        print("department",self.department)

employee =Employee("kjm",999999)
manager=Manager("jay",888888,"cse")
employee.display()
manager.display()
        
