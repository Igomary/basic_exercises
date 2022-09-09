# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки
from tokenize import group


print('Задание 1:')
names = ['Оля', 'Петя', 'Вася', 'Маша']
# ???
for each in names:
    print(each)

# Задание 2
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём
# Пример вывода:
# Оля: 3
# Петя: 4
print('\nЗадание 2:')
names = ['Оля', 'Петя', 'Вася', 'Маша']
# ???
for each in names:
    print(f'{each}: {len(each)}')

# Задание 3
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика
print(f'\nЗадание 3:')
is_male = {
    'Оля': False,  # если False, то пол женский
    'Петя': True,  # если True, то пол мужской
    'Вася': True,
    'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша']
# ???
for each in is_male:
    if each:
        print(f'{each}: male')
    else:
        print(f'{each}: female')

# Задание 4
# Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# Группа 1: 2 ученика.
# Группа 2: 4 ученика.
print('\nЗадание 4:')
groups = [
    ['Вася', 'Маша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
    ['Оля', 'Петя', 'Гриша'],
]

print(f'Всего {len(groups)} группы.')
i = 0
while i < len(groups):
    print(f'Группа {i+1}: {len(groups[i])} ученика')
    i += 1


# Задание 5
# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят
# Пример вывода:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша
print('\nЗадание 5:')
groups = [
    ['Вася', 'Маша'],
    ['Оля', 'Петя', 'Гриша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
]
i = 0
while i < len(groups):
    str = f'Группа {i+1}: '
    str +=', '.join(groups[i])
    print(str)
    i += 1

# ???