# print("Чи повнолітній користувач")
# age=int(input("Вкажіть ваш вік"))
# if age>17:
#     print("Користувач ПОВНОЛІТНІЙ")

def findgrade(Ball):
    if 0 <= ball <= 49:
        return "незадовільно"
    elif 50 <= ball <= 69:
        return "задовільно"
    elif 70 <= ball <= 89:
        return "добре"
    elif 90 <= ball <= 100:
        return "Відмінно"

ball = int(input("Введіть кількість балів: "))
grade = findgrade(ball)
print(f"Оцінка: {grade}")