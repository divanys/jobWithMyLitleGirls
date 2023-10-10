# Создать словарь, в котором ключами будут числа от 1 до 5, а значениями будет их буквенное название, например, 1 - "один"


word_numbers = ["один", "два", "три", "четыре", "пять"]

result_dict = {}

for i in range(len(word_numbers)):
    result_dict[i + 1] = word_numbers[i]

print(result_dict)