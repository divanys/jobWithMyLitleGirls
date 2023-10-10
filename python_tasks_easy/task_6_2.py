# Даны два списка чисел, которые могут содержать до 10 чисел каждый.
# Выведите все числа, которые входят как в первый, так и во второй список в порядке возрастания.

list1 = [1, 3, 5, 7, 9]
list2 = [2, 3, 4, 5, 6, 9, 1, 0]

set1 = set(list1)
set2 = set(list2)

common_numbers = set1.intersection(set2)
sorted_numbers = sorted(common_numbers)

print(sorted_numbers)
