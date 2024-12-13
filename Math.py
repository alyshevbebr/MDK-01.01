import math
import math as m 
# Задание 1
# import math
# ax**2 + bx + c = 0
# A = int(input("Введите число: "))
# B = int(input("Введите число: "))
# C = int(input("Введите число: "))
# D = m.pow(B, 2) - 4 * A * C
# print(f"D равен : {D}")
# if D == 0:
#     x = -B/(2*A)
#     print(x)
# elif D < 0:
#     print("Нет корней")
# else:
#     x1 = (-B + D**0.5) / 2*A
#     x2  =  (-B - D**0.5) / 2*A
#     print(x1,x2)

# Задание 2

AB = int(input("Введите число длины первого катета: "));AC = int(input("Введите число длины второго катета:  ")) 
BC = m.sqrt(m.pow(AB, 2) + m.pow(AC, 2))
S = (AB*AC)/2;P = AB + AC + BC
print(f"Площадь: {S}"); print(f"Периметр: {P}")

# Задание 3 
p=float(round(m.pi, 2))
r=float(input('Введите число: '))
print(p)
S=p * m.pow(r, 2)
print(S)


# Задание 4
ab = int(input("Первая сторона треугольника: "));bc= int(input("Второя сторона треугольника: "));ac = int(input("Третья сторона треугольника: "))
if (ab+bc) > ac:
    print("Треуольник существует")
else:
    print("Треуольник не  существует")
