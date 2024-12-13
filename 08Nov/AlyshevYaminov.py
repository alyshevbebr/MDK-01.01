# Задание 1
def is_even(num: int ) -> int:
    print("Четное") if num % 2 ==0 else print("Нечетное")
    return is_even

is_even(30)
# Задание 2
def age_category(age: int ) -> int :
    return "Детский" if age > 0 and age < 13 else  "Подростковый" if  age > 13 and age <  17 else "Взрослый"

print(age_category(20))
# Задание 3
def check_sign(num: int ) -> int:
    return "Положительное" if num > 0 else "Отрицательное " if num < 0 else "Ноль"

print(check_sign(-5))
#Задание 4
def grade_evaluation(mark : int ) -> int:
    return "Ужасно" if mark > 0 and mark <31 else "Нужно учиться " if mark > 30 and mark < 50 else "Хорошо" if mark > 50 and mark < 80 else  "Отлично" if mark > 80 and mark < 101 else "Ошибка"

print(grade_evaluation(100))
# Задание 5 
def greeting(hour: int ) -> int:
    return "Доброе утро" if hour > 4 and hour < 12 else "Добрый день" if hour > 12 and hour < 18 else "Добрый вечер " if hour > 18 and hour < 22 else "Доброй ночи" 

print(greeting(0))

# Задание 6
matem = int(input("Введите оценку за матем."))
russ = int(input("Введите оценку за русс. язык"))
eng = int(input("Введите оценку за англ."))
grd = (matem,russ,eng)
grd_averg = sum(grd) / len(grd)
def average_grade(marks:int) -> int:
    return "Низкий " if grd_averg > 0 and  grd_averg < 4 else "Средний" if grd_averg > 3 and grd_averg < 5 else "Высокий"
print(average_grade(grd_averg))

# Задание 7
def classify_number(num: int) -> int:
    return "Положительное нечетное" if num >0 and num % 2 != 0 else "Положительное четное" if num > 0 and num % 2 == 0 else "Отрицательное четное "if num <  0 and num % 2 == 0 else "Отрицательное нечетное" if num < 0  and num % 2 != 0 else "Ноль"
print(classify_number(-3))