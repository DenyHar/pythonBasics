# Завдання 1
num_list = [1, 9, 1, 0, 11, 2, 0, 2, 4, 4, 5]

tup = tuple(num_list)

n = int(input("Введіть число n: "))
result = [num for num in tup if num < n]

print(f"Отже числа менші за {n}: {result}")


# Завдання 2
shoping_list = "Milk", "Bread", "Eggs"
checklist = ', '.join(shoping_list)
print(f"Ваш список: {checklist}")


# Завдання 3
bookshelf = {
    "Алгоритми доступно": ("Томас Г. Кормен", 2021, 194),
    "Кобзар": ("Т. Г. Шевченко", 2023, 480),
    "Лісова пісня": ("Леся Українка", 2018, 256)
}

book_name = input("Яку книгу шукаєте? ")

if book_name in bookshelf:
    print(f"{book_name}, Автор: {bookshelf[book_name][0]}, Рік видання: {bookshelf[book_name][1]}, Кількість сторінок: {bookshelf[book_name][2]}")
else:
    print("Такой книги немає")


# Завдання 4
#Все вигадано, співпадіння випадкові
t_lastName = "Гарагуля", "Коваленко", "Мацюк", "Савченко"
t_course = 3, 3, 2, 3
t_group = "КІ-22-1", "ЕЛ-22-1", "КІ-23-1", "КІ-22-1"
t_avgScore = 81, 85, 79, 78
dict_list = {}

for n in range(len(t_lastName)):
    dict_list.update({t_lastName[n]: (t_course[n], t_group[n], t_avgScore[n])})

lastN = input("Прізвище студента: ")
if lastN in dict_list:
    print(f"{lastN}, Курс: {dict_list[lastN][0]}, Група: {dict_list[lastN][1]}, Середній бал: {dict_list[lastN][2]}")
else:
    print("Такого(-ї) студента(-ки) немає.")


# Завдання 5
#Для спрощення номери телефонів будуть п'ятизначними
phone_book = {"Андрій": (15463, 75943),
              "Богдан": (17642, 99954),
              "Анна": (77733, 62485),
              "Taxi": (88008, 55050, 96065)
              }

def addNumber(dict, key, num):
    dict[key] += num,

addNumber(phone_book, "Богдан", 19102)

print(phone_book)