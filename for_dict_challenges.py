# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

def list_names(students_group):
    list_new ={}
    for each in students_group:
        st_name = each['first_name']
        list_new[st_name] = list_new.get(st_name, 0) + 1
    return(list_new)

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
# ???

print('\nЗадание 1: ')
list_new = list_names(students)
list_new = dict(sorted(list_new.items()))

for key, value in list_new.items():
    print(f'{key}: {value}')
    



# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
# ???
print('\nЗадание 2: ')
list_new =list_names(students)
max_value = max(list_new.values())

for key, value in list_new.items():
    if value == max_value:
     print(f'Cамое частое имя среди учеников: {key}')




# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
# ???
print('\nЗадание 3: ')

i = 1

for students in school_students:

    list_new = list_names(students)
    max_value = max(list_new.values())

    for key, value in list_new.items():
        if value == max_value:
            print(f'Cамое частое имя в классе {i}: {key}')
    
    i += 1

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '3б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
# ???
print('\nЗадание 4: ')

for school_class in school:
    male = 0
    female = 0
    class_name = school_class['class']
    for each in school_class['students']:
        if is_male.get(each['first_name']):
            male += 1
        else:
            female += 1
    
    print(f'Класс {class_name}: девочки {female}, мальчики {male}')


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
# ???
print('\nЗадание 5: ')

school_new = []

for school_class in school:
    male = 0
    female = 0
    class_name = school_class['class']
    for each in school_class['students']:
        if is_male.get(each['first_name']):
            male += 1
        else:
            female += 1
    
    school_new.append({'class':class_name, 'male' : male, 'female' : female})

max_males = 0
max_females = 0
f_class_name = ''
m_class_name = ''

for each in school_new:
    if each['male'] > max_males:
        max_males = each['male']
        m_class_name = each['class']
    if each['female'] > max_females:
        max_females = each['female']
        f_class_name = each['class']

print(f'Больше всего мальчиков в классе {m_class_name}')
print(f'Больше всего девочек в классе {f_class_name}')