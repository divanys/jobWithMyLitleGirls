# Задание 4_3
# Введите строку с клавиатуры, переведите её в нижний регист и замените все буквы "а" на "е".

user_input = input("Введите строку: ")

modified_string = user_input.lower().replace('а', 'е')

print(f"Измененная строка: {modified_string}")
