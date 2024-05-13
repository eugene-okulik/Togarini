# Задание №1
# Создайте универсальный декоратор, который можно будет применить к любой
# функции. Декоратор должен делать следующее: он должен распечатывать
# слово "finished"после выполнения декорированной функции.

# Код, использующий этот декоратор может выглядеть, например, так:

# @finish_me
# def example(text):
#     print(text)

# example('print me')
# В результате работы будет такое:

# print me

# finished

def func_decorator(x):
    def wrapper(fin):
        result = x(fin)
        print('finished')
        return result

    return wrapper


@func_decorator
def example(text):
    print(text)


example('print me')


# Задание №2
# Создайте универсальный декоратор, который будет управлять тем, сколько раз
# запускается декорируемая функция

# Код, использующий этот декоратор может выглядеть, например, так:

# @repeat_me
# def example(text):
#     print(text)

# example('print me', count=2)
# В результате работы будет такое:

# print me

# print me

# Если есть время и желание погуглить и повозиться, то можно попробовать
# создать декоратор, который сможет обработать такой код:

# @repeat_me(count=2)
# def example(text):
#     print(text)

# example('print me')


def repeat_me(f):
    def wrapper(text, **y):
        count = y.pop('count', 1)
        for _ in range(count):
            f(text, **y)
    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count=2)


# Задание №3
# Напишите программу: Есть функция которая делает одну из арифметических
# операций с переданными ей числами (числа и операция передаются в аргументы
# функции). Функция выглядит примерно так:

# def calc(first, second, operation):
#     if operation == '+':
#         return first + second
#     elif .....
# Программа спрашивает у пользователя 2 числа (вне функции)

# Создайте декоратор, который декорирует функцию calc и управляет тем какая
# операция будет произведена:

# если числа равны, то функция calc вызывается с операцией сложения этих чисел
# если первое больше второго, то происходит вычитание второго из певрого
# если второе больше первого - деление первого на второе
# если одно из чисел отрицательное - умножение

first = int(input('first = '))
second = int(input('second = '))


def comp():
    def wrapper(*f):
        if first == second:
            return calc(first, second, '+')
        elif first > second:
            return calc(first, second, '-')
        elif second > first:
            return calc(first, second, '/')
        elif first < 0:
            return calc(first, second, '*')
    return wrapper


def calc(first, second, operation):
    operations = {
        '+': lambda: first + second,
        '-': lambda: first - second,
        '/': lambda: first / second,
        '*': lambda: first * second
    }
    return operations.get(operation)()


print(comp()(first, second))


# List comprehension
# Дан такой кусок прайс листа:

# (Копируйте эту переменную (константу) в код прямо как есть)

# PRICE_LIST = '''тетрадь 50р
# книга 200р
# ручка 100р
# карандаш 70р
# альбом 120р
# пенал 300р
# рюкзак 500р'''
# При помощи генераторов превратите этот текст в словарь такого вида:

# {'тетрадь': 50, 'книга': 200, 'ручка': 100, 'карандаш': 70, 'альбом': 120,
# 'пенал': 300, 'рюкзак': 500}
# Обратите внимание, что цены в словаре имеют тип int (они не в кавычках)


PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

text = PRICE_LIST.strip().split('\n')
# dict = {}
# for x in text:
#     key, value = x.split()
#     dict[key] = int(value[:-1])
dict = {key: int(value[:-1]) for key in text for key, value in [key.split()]}
print(dict)
