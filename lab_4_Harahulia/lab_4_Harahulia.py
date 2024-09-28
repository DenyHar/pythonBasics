n = int(input("Введіть n: "))
print(n >= 100)

a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
if a > b:
    print(a, "більше")
else:
    print(b, "більше")

plant = input("Введіть назву рослини (латиницею): ")
if plant == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif plant == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else: print("Spathiphyllum! Not " + plant + '!')

income = float(input("Enter the annual income: "))

#
# Write your code here.
if income <= 85528:
    tax = 18 * income / 100 - 556.02
else:
    tax = 32 * (income - 85528) / 100 + 14839.02
if tax < 0: tax = 0.0
#

tax = round(tax, 0)
print("The tax is:", tax, "thalers")

year = int(input("Введіть рік: "))

if year < 1582: print("Not within the Gregorian calendar period.")
elif year % 4 != 0:
    print("Common year")
elif year % 100 != 0:
    print("Leap year")
elif year % 400 != 0:
    print("Common year")
else: print("Leap year")

secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
prisoner_number = int(input("Таємне число ... "))
while prisoner_number != secret_number:
    print("Ха-ха! Ви застрягли у моїй петлі!")
    print("Спробуй ще раз, може пощастить)")
    prisoner_number = int(input("Нехай буде ... "))
print(str(prisoner_number) + '!')
print("Молодець, магле! Тепер ти вільний")

import time

for i in range(1, 6):
    print(str(i) + " Mississippi")
    time.sleep(1)
print("Ready or not, here I come!")

while True:
    word = input("Введіть слово: ")
    if word == "chupacabra": break
print("You've successfully left the loop.")

user_word = input("Введіть слово: ")
user_word = user_word.upper()

for letter in user_word:
    if letter == 'A': continue
    elif letter == 'E': continue
    elif letter == 'I': continue
    elif letter == 'O': continue
    elif letter == 'U': continue
    else: print(letter)

user_word = input("Введіть слово: ")
user_word = user_word.upper()
word_without_vowels = ""

for letter in user_word:
    if letter == 'A': continue
    elif letter == 'E': continue
    elif letter == 'I': continue
    elif letter == 'O': continue
    elif letter == 'U': continue
    else: word_without_vowels += letter
print(word_without_vowels)

bricks_amount = int(input("Введіть кількість цеглин: "))
height = 1
while True:
    bricks_amount -= height
    if bricks_amount < 0:
        height -= 1
        break
    elif bricks_amount == 0: break
    height += 1
print("The height of the pyramid:", height)

c0 = int(input("Введіть натуральне число: "))
steps = 0

while c0 != 1:
    if c0 % 2 == 0:
        c0 /= 2
    elif c0 % 2 != 0:
        c0 = 3 * c0 + 1
    print(int(c0))
    steps += 1
print("steps =", steps)

x, y, z = 5, 10, 8
x, y, z = z, y, x
print(x > z)
print((y-5)==x)