# name = input("Введите свое значение: "); age = input("Введите свое значение: ")
# print(f'Привет, {name}!, Тебе {age} лет!')

# goroda = ["Tymen, Kazan, Moskow, Ekaterinburg, Peterburg"]; a = ", ".join(goroda)
# print(a)

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(3))

def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 5:
        return 120
    else: 
        return n * factorial(n-1)
print(factorial(5))
