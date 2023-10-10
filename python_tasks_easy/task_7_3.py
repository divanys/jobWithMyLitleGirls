# Задание 7_3
# Дан словарь с числовыми значениями. Необходимо их все перемножить и вывести на экран.

my_dict = {'a': 2, 'b': 3, 'c': 4}

mult = 1

for value in my_dict.values():
    mult *= value

print(mult)