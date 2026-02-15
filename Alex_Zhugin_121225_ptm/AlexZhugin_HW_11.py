# Звёздочки вместо чисел
# Напишите программу, которая заменяет все цифры в строке на звёздочки *.
# text = "My number is 123-456-789"
# Пример вывода:
# Строка: My number is 123-456-789
# Результат: My number is ***-***-***


# text = "My number is 123-456-789"
#
# for d in "0123456789":
#     text = text.replace(d, "*")
#
# print("Результат:", text)



# Количество символов
# Напишите программу, которая подсчитывает количество вхождений всех символов в строке.
# Нужно вывести только символы, которые встречаются более 1 раза (игнорируя регистр),
# с указанием их количества. Выводите повторяющиеся символы только один раз.
# text = "Programming in python"
# Пример вывода:
# Строка: Programming in python
# Символ 'p' встречается 2 раз(а)
# Символ 'r' встречается 2 раз(а)
# Символ 'o' встречается 2 раз(а)
# Символ 'g' встречается 2 раз(а)
# Символ 'm' встречается 2 раз(а)
# Символ 'i' встречается 2 раз(а)
# Символ 'n' встречается 3 раз(а)
# Символ ' ' встречается 2 раз(а)


# text = "Programming in python"
#
# print("Строка:", text)
#
# low = text.lower()
#
# for x in low:
#     if low.count(x) > 1:
#         print("Символ", x, "встречается", low.count(x), "раз(а)")
#         low = low.replace(x, "")




# Увеличение чисел
# Напишите программу, которая заменяет все числа в строке на их эквивалент, умноженный на 10.
# text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
# Пример вывода:
# I have 50.0 apples and 100.0 oranges, price is 5.0 each. Card number is ....3672.

# text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
# words = text.split()
# res = ""
# for x in words:
#     tmp = x.strip(".,")
#     if tmp.replace(".", "", 1).isdigit():
#         num = float(tmp) * 10
#         res = res + x.replace(tmp, str(num)) + " "
#     else:
#         res = res + x + " "
# print(res.strip())
