# Задание 2_1
# Написать программу, вычисляющую сумму последовательности чисел 1, 3, 5, 7, n
# n - вводится с клавиатуры

n = int(input("Введите n: "))

total = 0

for i in range(1, n + 1, 2):
    total += i

print(f"Сумма последовательности: {total}")
