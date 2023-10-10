# Написать формулу покупки в магазине - 2 булочки стоимостью 35 рублей, 1 чай - 20 рублей


def form(count_of_bun, count_of_tea):
    sum_all = (count_of_bun * 35 / 2) + count_of_tea * 20

    return sum_all


print(f"Сумма покупки 2 булочекmult_of_evens и 1 чая в магазине равна {form(2, 1)}")
