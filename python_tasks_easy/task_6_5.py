# Напишите программу, которая получает на вход две строки с перечислением интересов и хобби двух пользователей и вычисляет процент совпадания.


def calc(user1_interests, user2_interests):
    user1_interests_set = set(user1_interests.split(", "))
    user2_interests_set = set(user2_interests.split(", "))

    common_interests = user1_interests_set.intersection(user2_interests_set)

    similarity_percentage = (len(common_interests) / len(user1_interests_set)) * 100

    return similarity_percentage


user1_interests = input("Введите интересы первого пользователя (через запятую и пробел): ")
user2_interests = input("Введите интересы второго пользователя (через запятую и пробел): ")

percentage = calc(user1_interests, user2_interests)
print(f"Процент совпадения интересов: {percentage}%")

# книги, спорт, кулинария
# кино, спорт, книги, путешествия
