# # Завдання 1
#
# def is_hidden(string1, string2):
#     check = ""
#     index = 0
#     for letter in string1:
#         index = string2.find(letter, index)
#         if index != -1:
#             check += letter
#             continue
#     if check == string1:
#         return True
#     else: return False
#
# word = input("Введіть слово: ")
# code = input("Введіть рядок: ")
#
# if is_hidden(word, code):
#     print("Yes")
# else: print("No")

# Обчислює число "життя": суму цифр повної дати народження

# date = input("Введіть дату народження у форматі YYYYMMDD:")
# while True:
#     try:
#         sum = 0
#         for simbol in date:
#             sum += int(simbol)
#
#         date = str(sum)
#
#         if len(date) == 1:
#             break
#     except:
#         print("Схоже останій ввід був не правильним. Спробуйте ще раз")
#         date = input("Введіть дату народження у форматі YYYYMMDD:")
#
# print(sum)

# Завдання 3

def is_in_range(num, max, min):
    try:
        numb = int(num)
    except:
        print("Error: wrong input")
        raise TypeError
    if (max < numb) or (numb < min):
        print(f"Error: the value is not within permitted range ({min}..{max})")
        raise ValueError
    else: return print(num)

min = 3
max = 9
while True:
    number = input("Введіть число: ")
    try:
        is_in_range(number, max, min)
        break
    except:
        print("Спробуйте ще раз.")