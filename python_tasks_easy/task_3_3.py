# Задание 3_3
# Найти сумму чётных чисел от 1 до 100 включительно

def sum_of_evens(start, end):
    total = 0
    for i in range(start, end + 1):
        if i % 2 == 0:
            total += i
    return total


result = sum_of_evens(1, 100)

print(f"Сумма чётных чисел от 1 до 100 равна {result}")
