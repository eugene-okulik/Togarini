res_ops_1 = 'результат операции: 42'
res_ops_2 = 'результат операции: 514'
res_ops_3 = 'результат работы программы: 9'
addit = 10

res_ops_1_search = res_ops_1.index(':')
res_ops_2_search = res_ops_2.index(':')
res_ops_3_search = res_ops_3.index(':')

addit_res_ops_1 = int(res_ops_1[res_ops_1_search + 1:]) + addit
addit_res_ops_2 = int(res_ops_2[res_ops_2_search + 1:]) + addit
addit_res_ops_3 = int(res_ops_3[res_ops_3_search + 1:]) + addit

print(addit_res_ops_1, addit_res_ops_2, addit_res_ops_3)

person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(name, last_name, city, phone, country)

students = ['Ivanov', 'Petrov', 'Sidor']
subjects = ['math', 'biology', 'geography']

students_f_string: str = ', '.join(students)
subjects_f_string: str = ', '.join(subjects)

print(f'Students {students_f_string} study these subjects: {subjects_f_string}')

phrase = 'Students {0} study these subjects: {1}'
print(phrase.format(students_f_string, subjects_f_string))
