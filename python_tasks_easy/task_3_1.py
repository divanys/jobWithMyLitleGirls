# Найти с помощью функции произведение трёх чисел, вводимых с клавиатуры

num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))


def mult(num1, num2, num3):
    result = num1 * num2 * num3
    return result


print(f"Произведение чисел: {mult(num1, num2, num3)}")
