person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(name, last_name, city, phone, country)

res_ops_1 = 'результат операции: 42'
res_ops_2 = 'результат операции: 514'
res_ops_3 = 'результат работы программы: 9'
addit = 10
res_ops_my_1 = int(res_ops_1[res_ops_1.find('42'):]) + addit
res_ops_my_2 = int(res_ops_2[res_ops_2.index('514'):]) + addit
# res_ops_my_3_len = len(res_ops_3) == Длинна строки
# print(res_ops_my_3_len) == 29
res_ops_my_3 = int(res_ops_3[28]) + addit
# res_ops_my_3_1 = int(res_ops_3[-1]) + addit == 19
# print(type(res_ops_my_3)) == <class 'int'>
print(res_ops_my_1, res_ops_my_2, res_ops_my_3)

students = ['Ivanov', 'Petrov', 'Sidor']
subjects = ['math', 'biology', 'geography']

students_f_string: str = ', '.join(students)
subjects_f_string: str = ', '.join(subjects)

print(f'Students {students_f_string} study these subjects: {subjects_f_string}')

phrase = 'Students {0} study these subjects: {1}'
print(phrase.format(students_f_string, subjects_f_string))
