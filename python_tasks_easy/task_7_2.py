# Задание 7_2
# Создайте словарь, в котором ключами будут числа от 1 до 10, а значениями эти же числа в виде строки.


string_dict = {}

for i in range(1, 11):
    string_dict[i] = str(i)

print(string_dict)
