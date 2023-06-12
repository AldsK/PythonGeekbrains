# # Задача 22
import random
numbers_1 = set(random.randint(1, 100) for i in range(int(input('Введите количество цифр: '))))
numbers_2 = (random.randint(1, 100) for i in range(int(input('Введите количество цифр: '))))
result = sorted(numbers_1.intersection(numbers_2))
print(result)

# Задача 24
list_1 = [int(input('Введите к-во ягод на кусте: ')) for i in range(int(input('Введите к-во кустов черники: ')))]
arr_count = list()
for i in range(len(list_1)):
       arr_count.append(list_1[i-2] + list_1[i-1] + list_1[i])
print(max(arr_count))