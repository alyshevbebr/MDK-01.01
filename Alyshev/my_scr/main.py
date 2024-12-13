class Calculation():


    def sum(self, a, b):
        return a + b


    def sub(self, a, b):
        return a - b


    def multiply(self, a, b):
        return a * b


    def div(self, a, b):
        return a / b


    def find_palyndrome(self, arg: input) -> bool:
        arg = input()
        return arg == arg[::-1]




class Text_Greeting():
    def greeting(self, name: input) -> str:
        return f"My name {name}"


    def empty_string(self, arg: input) -> str:
        arg = input()
        return len(arg) > 0


    def register_check(self, arg: input) -> bool:
        arg = input()
        return arg == str.capitalize(arg)






    def  long_check(self, arg: input) -> bool:
        arg = input()
        return len(arg) < 10


    def string_type(self, arg: any) -> bool: #Пометка для себя Any(Любой тип данных), а isistance проверка является ли arg строкой
        arg = input()
        return not isinstance(arg, str)






