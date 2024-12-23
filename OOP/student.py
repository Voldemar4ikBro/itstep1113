import random

class Student:
    def __init__(self, name):
        self.name = name
        self.progress = 0
        self.lvlife = True
        self.mood = 50
        self.money = 100

    # методи класу
    def study(self):
        print("Час для навчання")
        self.progress += random.randint(3, 10)
        self.mood -= random.randint(1, 7)
        self.money -= random.randint(5, 10)  # витрати під час навчання

    def sleep(self):
        print("Час для сну")
        self.mood += random.randint(3, 10)

    def rest(self):
        print("Час для відпочинку")
        self.progress -= random.randint(1, 7)
        self.mood += random.randint(3, 10)
        self.money -= random.randint(10, 20)  # витрати під час відпочинку

    def work(self):
        print("Час для роботи")
        self.money += random.randint(20, 50)
        self.mood -= random.randint(3, 7)
        self.progress -= random.randint(1, 5)

    def isLvlife(self):
        if self.progress < 4:
            print("Ймовірність виключення із закладу")
            self.lvlife = False
        elif self.mood < 10:
            print("Студент в депресії")
            self.lvlife = False
        elif self.money < 0:
            print("Немає грошей")
            self.lvlife = False

    def everyday(self):
        print("\033[33mУспішність: ", self.progress, "\nНастрій: ", self.mood, "\nГроші: ", self.money, "\033[0m")

    def decide_action(self):
        if self.money < 20:
            return self.work
        elif self.progress < 10:
            return self.study
        elif self.mood < 30:
            return self.rest
        else:
            return random.choice([self.study, self.rest, self.sleep])

    def lifeStud(self, day):
        day = "\033[34mдень №" + str(day) + "\033[0m"
        print(day)
        action = self.decide_action()
        action()
        self.everyday()
        self.isLvlife()

st1 = Student("Сашко")
print("\033[33mСтуденське життя:", st1.name, "\n\033[0m")
for i in range(1, 366):
    if not st1.lvlife:
        break
    st1.lifeStud(i)

st2 = Student("Маринка")
print("\n\n\033[33mСтуденське життя:", st2.name, "\n\033[0m")
for i in range(1, 366):
    if not st2.lvlife:
        break
    st2.lifeStud(i)
