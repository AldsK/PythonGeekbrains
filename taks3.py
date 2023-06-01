import random
# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     3
#     -> 1

my_list = [int(input(f'Введите число:')) for i in range(int(input('Введите количество элементов: ')))]
print(my_list.count(int(input('Введите число Х: '))))

#Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     6
#     -> 5
#
numbers = [random.randint(1, 10) for i in range(int(input('Введите количество элементов: ')))]
print(numbers)
x = int(input('Введите число X: '))
first_num = abs(x - numbers[0])
index = 0
for i in range(len(numbers)):
    second_num = abs(x - numbers[i])
    if second_num < first_num:
        first_num = second_num
        index = i
print(f'Ближайшее число: {numbers[index]}')



# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.

eng = 'qwertyuiopasdfghjklzxcvbnm'

rus = 'йцукенгшщзхъфывапролджэячсмитьбюё'

list_English = {1:'AEIOULNSTR', 2:'DG', 3:'BCMP',
                4:'FHVWY', 5:"K" , 8:'JX', 10:'QZ'}
list_Russian = {1:'АВЕИНОРСТ', 2:'ДКЛМПУ', 3:'БГЁЬЯ',
                4:'ЙЫ', 5:'ЖЗХЦЧ', 8:'ШЭЮ', 10:'ФШЪ'}

eng = 'qwertyuiopasdfghjklzxcvbnm'

rus = 'йцукенгшщзхъфывапролджэячсмитьбюё'

eng_dic = {1:'AEIOULNSTR', 2:'DG', 3:'BCMP',
                4:'FHVWY', 5:"K" , 8:'JX', 10:'QZ'}
rus_dic = {1:'АВЕИНОРСТ', 2:'ДКЛМПУ', 3:'БГЁЬЯ',
                4:'ЙЫ', 5:'ЖЗХЦЧ', 8:'ШЭЮ', 10:'ФШЪ'}

word = input('Введите слово на русском или английском языке: ')

if word[0].lower() in eng:
    total = 0
    for letter in word:
        for key, value in eng_dic.items():
            if letter.upper() in value:
                total += key
    print(f'стоимость введенного английского слова = {total}')
else:
    if word[0].lower() in rus:
        total = 0
        for letter in word:
            for key, value in rus_dic.items():
                if letter.upper() in value:
                    total += key
    print(f'стоимость введенного русского слова = {total}')



