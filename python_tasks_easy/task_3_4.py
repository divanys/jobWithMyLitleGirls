# Задание 3_4
# Найти произведение чисел от 7 до 29 включительно

def mult_of_num(start, end):
    mult = 1
    for i in range(start, end + 1):
        mult *= i
    return mult


result = mult_of_num(7, 29)

print(f"Произведение чисел от 7 до 29 равно {result}")
