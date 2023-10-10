# Задание 4_1
# Введите 2 строки с клавиатуры - объедините их и подсчитайте количество любого символа.


string1 = input("Введите первую строку: ")
string2 = input("Введите вторую строку: ")

combined_string = string1 + string2

char_to_count = input("Введите символ для подсчета: ")

count = combined_string.count(char_to_count)

print(f"Количество символа '{char_to_count}' в объединенной строке равно {count}")
