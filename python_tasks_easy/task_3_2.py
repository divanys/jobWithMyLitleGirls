# Задание 3_2
# Найти факториал числа 12

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


number = 12
result = factorial(number)

print(f"Факториал числа {number} равен {result}")
