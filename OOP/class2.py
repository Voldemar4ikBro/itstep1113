# class People:
#     def __init__(self, name="Passenger",age=None):
#         self.name = name
#         self.age = age
# class Bus:
#     def __init__(self, model):
#         self.model = model
#         self.Passenger=[]
#     def add(self,human):
#         self.Passenger.append(human)
#     def info(self):
#         if self.Passenger!=[]:
#             print("Автобус (", self.model,") має пасажирів:")
#             for i in self.Passenger:
#                 print(i.name)
#         else:
#             print("Автобус (",self.model, ") НЕМАЄ пасажирів:")
#
# p1=People("Петро", 12)
# p2=People("Катя", 10)
# b1=Bus("DAF")
# b1.add(p1)
# b1.add(p2)
# b1.info()

import random

class human:
    def __init__(self, name,job,home,car):
        self.name = name
        self.job = job
        self.home = home
        self.car = car
    def getHome(self):
        pass
    def getJob(self):
        pass
    def getCar(self):
        pass
    def repairCar(self):
        pass
    def indexDay(self,day):
        pass
    def isLvLife(self):
        pass
    def life(self):
        pass
class auto:
    def __init__(self,model_list):
        self.model = random.choice(list(model_list)) #випадкова модель
        self.color = model_list[self.model]["колір:"]
        self.color = model_list[self.model]["рік:"]
        self.color = model_list[self.model]["об'єм двигуна:"]
class Work:
    def __init__(self,job_list):
        self.job = random.choice(list(job_list))
        self.exp = job_list[self.job]["стаж:"]
        self.lvl = job_list[self.job]["рівень:"]
        self.salary = job_list[self.job]["зарплата:"]
class House:
    def __init__(self):
        self,food=0
ModelCar={
    "volkswagen":{"колір:":"білий","рік":2022,"об'єм двигуна:":1.6},
    "Volvo":{"колір:":"білий","рік":2017,"об'єм двигуна:":2.0},
    "Nissan":{"колір:":"жовтий","рік":2012,"об'єм двигуна:":1.5},
}
JobHuman={
    "розробник Python":{"стаж:":5,"рівень:":"Senior","зарплата:":6500},
    "веб-дизайнер":{"стаж:":3,"рівень:":"Middle","зарплата:":3500},
    "системний адміністратор":{"стаж:":10,"рівень:":"Senior","зарплата:":4000}
}