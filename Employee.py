print("Employee info collector")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
role = input("Enter your role: ")
department = input("Enter your department: ")
salary = float(input("Enter your salary: "))
class Employee:
    def __init__(self,role,department,salary):
        self.role = role
        self.department = department
        self.salary =  salary
    def showDetails(self):
        print("Role:",self.role)
        print("Department:",self.department)
        print("Salary:",self.salary)
class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__(role,department,salary)
    def show_engg(self):
        print("Name:", self.name)
        print("Age:", self.age)
engg = Engineer("Mohan", 34)
engg.show_engg()
engg.showDetails()
