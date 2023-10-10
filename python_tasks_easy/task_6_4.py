# Даны два множества E = {14, "maximum", "minimum"} и F = {14, "maximum", "min"}.
# Сравните их.

E = {14, "maximum", "minimum"}
F = {14, "maximum", "min"}


if E == F:
    print("Множества E и F равны")
else:
    print("Множества E и F не равны")

if E <= F:
    print("E является подмножеством F")
else:
    print("E не является подмножеством F")

if F <= E:
    print("F является подмножеством E")
else:
    print("F не является подмножеством E")