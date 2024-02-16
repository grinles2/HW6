from random import choice


class Randomaizer:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def __random_operation(self):
        temp = ["*", "-", "+"]
        #словарь
        operation = choice(temp)
        if operation == "*":
            return self.__a * self.__b
        elif operation == "-":
            return self.__a - self.__b
        elif operation == "+":
            return self.__a + self.__b

    def get_result(self):
        return self.__random_operation()
a = 2
b = 5
r = Randomaizer(a, b)
print(r.get_result())