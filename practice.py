"""class method as constructor"""
class person:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
    @classmethod
    def info_string(cls, string):
        return  cls(string.split("-")[0],int(string.split("-")[1]),float(string.split("-")[2]))
    @classmethod
    def info_underscore(cls, underscore):
        return  cls(underscore.split("_")[0],int(underscore.split("_")[1]),float(underscore.split("_")[2]))
p1 = person("shiva",12,88.3)
print(p1.name, p1.age, p1.marks)

p2 = person.info_string("mukesh-34-69.99")
print(p2.name, p2.age, p2.marks)

p3 = person.info_underscore("rajesh_32_77.88")
print(p3.name, p3.age, p3.marks)