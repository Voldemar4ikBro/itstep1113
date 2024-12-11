# class Human:
#     def __init__(self, name, age, city):
#         self.name = name
#         self.age = age
#         self.city = city
#     def info(self):
#         print("Вітаю Мене звати",self.name,"мені", self.age,"я з міста", self.city)
# class People(Human):
#     def __init__(self, name, age, city, classroom):
#         super().__init__(name, age, city)
#         self.classroom = classroom
#     def study(self):
#         return self.name +" я навчаюся у "+ str(self.classroom)+" класі"
# class Student(Human):
#     def __init__(self, name, age, city, kyrs, universtitet):
#         super().__init__(name, age, city)
#         self.kyrs = kyrs
#         self.universtitet = universtitet
#     def studyUN(self):
#         return self.name + " я навчаюся у " + str(self.kyrs) + " курс "+ self.universtitet+" університет"
# h1=Human("Антон",12,"Запоріжжя")
# h1.info()
# p1=People("Яна",12,"Дніпро",7)
# print(p1.study())
# p1.info()
# s1=Student("Володимир",16,"Харьків",1,"ХНУ")
# print(s1.studyUN())
# s1.info()
class PC:
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.memory=256
class Display:
    def __init__(self):
        super().__init__()
        self.resolution="4K"
class Smart(PC,Display):
    def info(self):
        print("Смарт моделі",self.model,"має параметри:",self.memory,"МБ пам'яти та розширення дисплея",self.resolution)
phone1=Smart("iPhone")
phone1.info()