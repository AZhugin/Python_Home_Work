# Напишите программу, которая обрабатывает список из строк и удаляет все строки, содержащие более одного слова,
# а также преобразует оставшиеся строки к нижнему регистру.
# Данные:
#
# text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
#
# Пример вывода:
# Обработанный список: ['hello', 'world', 'simple']

text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]

text_list_new = []

for text in text_list:
    if len(text.split()) == 1:
        text_list_new.append(text.lower())

print("Обработанный список:", text_list_new)

# Обновление цен товаров. Дан список товаров с ценами.
# Программа должна применить скидку к каждому товару и добавить в список элемент с новой ценой.
# В конце вывести таблицу с новой ценой.
#
# Данные:
# products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]
#
# Пример вывода:
# Введите скидку (в процентах): 17

products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]

sale = float(input("Введите скидку (в процентах): "))

print(f"{'Товар':<12} {'Старая цена':>13} {'Новая цена':>13}")

for product in products:
    name = product[0]
    price = product[1]
    new_price = price * (1 - sale / 100)
    print(f"{name:<12} {price:>12.2f}$ {new_price:>12.2f}$")
