from random import choice
class Randomaizer:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def __random_operation(self):
        temp = ["*", "-", "+"]
        operation = choice(temp)
        if operation == "*":
            return self.__a * self.__b
        elif operation == "-":
            return self.__a - self.__b
        elif operation == "+":
            return self.__a + self.__b

    def __number(self): # Получение чисел
        a = int(input())
        b = int(input())
        r = Randomaizer(a, b)

#Обьект Класса
numbers = Randomaizer()
numbers.__number() # вызов


#вывод

