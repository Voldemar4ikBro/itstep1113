from tokenize import group


class Student:
    # print("Привіт, створення класу")
    def __init__(self, name="Someone", group="1113", age=13): #self- посилатися на себе на клас
        self.name=name
        self.group=group
        self.age=age
    def __str__(self):
        return "Ім'я студента:"+self.name+"навчаэться у групы"+self.group+str(self.age)
st1=Student()
print(st1.name, st1.group ,st1.age)
st2=Student()
print(st2.name, st2.group ,st2.age)
print(st2)