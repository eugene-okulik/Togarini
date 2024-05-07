# Обработка даты
# Дана такая дата: "Jan 15, 2023 - 12:05:33"

# Преобразуйте эту дату в питоновский формат, после этого:

# 1. Распечатайте полное название месяца из этой даты

# 2. Распечатайте дату в таком формате: "15.01.2023, 12:05"
import datetime


py_date = datetime.datetime(2023, 1, 15, 12, 5, 33)
full_month = py_date.strftime('%B')
print_date = py_date.strftime('%d.%m.%Y, %H:%M')

print(py_date)
print(full_month)
print(print_date)


# Map, filter
# Есть такой список:

# temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27,
# 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]
# С помощью функции map или filter создайте из этого списка новый список с
# жаркими днями. Будем считать жарким всё, что выше 28.

# Распечатайте из нового списка самую высокую температуру,
# самую низкую и среднюю.

temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22,
                22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]

hot_days = filter(lambda x: x > 28, temperatures)
hot_days_etc = []
for x in temperatures:
    if x > 28:
        hot_days_etc.append(x)

print(list(hot_days))
print(max(hot_days_etc))
print(min(hot_days_etc))
print(round(sum(hot_days_etc) / len(hot_days_etc), 2))
