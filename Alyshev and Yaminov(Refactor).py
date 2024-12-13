import time 
Hour = 5 
Time = 0
while Time <=30:
    print(Time)
    Time += 1
    if Hour == Time:
        time.sleep (1)
        print(Hour+Time)

def calculate(x, y, operator):
    if operator == "1":
        return (x+y)
    if operator == "2":
        return (x-y)
    if operator == "3":
        return (x*y)
    if operator == "4":
        return (x/y)
def divide(x,y):
    if y != 0:
        return x / y
    else:
        print("Ошибка: деление на ноль!")
        return None
print("Выберите операцию:")
while True:
    print("1. Сложение");print("2. Вычитание");print("3. Умножение");print("4. Деление")
    choice = input("Введите номер операции (1/2/3/4): ")
    if choice in ['1', '2', '3', '4']:
        break
    else:
        print("Ошибка: неверный ввод!")
num1 = float(input("Введите первое число: "));num2 = float(input("Введите второе число: "))
result = calculate(num1, num2, choice)
print(result)
