class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.make} {self.model} {self.year}"

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_salary_info(self):
        return f"Заробітна плата {self.name}: {self.salary}"

car = Car("Volvo", "c30", 2006)
print(car.get_info())
Employee = Employee("Володимир", "Designer", 3000)
print(Employee.get_salary_info())
