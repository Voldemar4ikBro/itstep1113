#симулятор життя студента
import random

class Student:
    def __init__(self, name):
        self.name=name
        self.progress=0 #100
        self.lvlife=True
        self.mood=50 #100

    # методи класу
    def study(self):
        print("Час для навчання")
        self.progress+=random.randint(3,10)
        self.mood-=random.randint(1,7)
    def sleep(self):
        print("Час для сну")
        self.mood -= random.randint(1, 7)
    def rest(self):
        print("Час для відпочинку")
        self.progress -= random.randint(1, 7)
        self.mood += random.randint(3, 10)
    def isLvlife(self):
        if self.progress<4:
            print("Ймовірність виключення із закладу")
            self.lvlife=False
        elif self.progress<9:
            print("Підготовка до сесії\nБезсонні ночі")
            self.lvlife=False
        elif self.progress<13:
            print("Екзамен екстерном \nЗбільшення часу на відпочинок")
            self.lvlife = False

    def everyday(self):
        print("\033[33mУспішність: ", self.progress, "\nНастрій: ", self.mood,"\033[0m")
    def lifeStud(self, day):
        day="\033[34mдень №"+str(day)+"\033[0m"
        rnd=random.randint(1,3)
        print(day)
        if rnd==1:
            self.study()
        elif rnd==2:
            self.sleep()
        elif rnd==3:
            self.rest()
            self.everyday()
            self.isLvlife()

st1=Student("Сашко")
#print(st1.name, "Успішність: ", st1.progress, st1.lvlife, "Настрій: ", st1.mood)
print("\033[33mСтуденське життя:", st1.name, "\n\033[0m") #30-37 цвет текста, 40-47 цвет фона
for i in range(1, 31):
    if st1.lvlife==False:
        break
    st1.lifeStud(i)

st2=Student("Маринки")
#print(st1.name, "Успішність: ", st1.progress, st1.lvlife, "Настрій: ", st1.mood)
print("\n\n\033[33mСтуденське життя:", st2.name, "\n\033[0m") #30-37 цвет текста, 40-47 цвет фона
for i in range(1, 31):
    if st2.lvlife==False:
        break
    st2.lifeStud(i)