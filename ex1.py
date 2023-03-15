'''
Изучение pandas
'''

import pandas as pd

# Series - это создание одномерного массива данных одного типа. Можно задавать свои ключи
t = pd.Series([1, 3, 4]) 
print(t)

print('+*+*+*+*+*+*+*+*+*+')

g = {'eat': 'cookies', 'drink': 'tea', 'sleep': 'bed'}
n = pd.Series(g)
print(n)
print(n.values)
# выполнение арифметических операций с Series 

print(t * 5)
print('+*+*+*+*+*+*+*+*+*+')
print(t / 5)
print('+*+*+*+*+*+*+*+*+*+')
print(t == 1)

print(sorted(t), sorted([3, 6, 1]))

print(t.index)


# работа с DataFrame

df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [
            22,
            35,
            58
        ],
        "Sex": [
            "male",
            "male",
            "female"
        ],
    }
)

print(df)

df2 = pd.DataFrame.from_dict({'a': [3, 4, 5], 'b': [1, 7, 2]})
print(df2)

dfmi = pd.DataFrame([list('abcd'),
                     list('efgh'),
                     list('ijkl'),
                     list('mnop')],
                    columns=pd.MultiIndex.from_product([['one', 'two'],
                                                        ['first', 'second']]))

print(dfmi.loc[:, ('one', 'second')])
