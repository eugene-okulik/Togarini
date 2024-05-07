# Напишите программу. Есть две переменные, salary и bonus.
# Salary - int, bonus - bool. Спросите у пользователя salary.
# А bonus пусть назначается рандомом.

# Если bonus - true, то к salary должен быть добавлен рандомный бонус.

# Примеры результатов:

# 10000, True - '$10255'
# 25000, False - '$25000'
# 600, True - '$3785'

import random

salary = int(input("Input your salary: "))
bonus = random.choice([True, False])
bonus_salary = random.uniform(1, 3)

if bonus:
    salary_with_bonus = int(salary * bonus_salary)
    print(f"{salary}, {bonus} - '${salary_with_bonus}'")
else:
    print(f"{salary}, {bonus} - '${salary}'")


# Напишите функцию-генератор, которая генерирует
# последовательность чисел фибоначчи
# Распечатайте из этого списка пятое число, двухсотое число, тысячное число,
# стотысячное число
def fibonacci_sequence():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fibonacci = fibonacci_sequence()

for i in range(5):
    next(fibonacci)
print(next(fibonacci))

for i in range(200):
    next(fibonacci)
print(next(fibonacci))

for i in range(1000):
    next(fibonacci)
print(next(fibonacci))

for i in range(10000):
    next(fibonacci)
print(next(fibonacci))
