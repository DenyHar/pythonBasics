hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.
hat_list[2] = int(input("Давайте замінимо середнє число в капелюсі. \nВведіть нове число: "))
# Step 2: write a line of code that removes the last element from the list.
del hat_list[-1]
# Step 3: write a line of code that prints the length of the existing list.
print("Наразі в капелюсі", len(hat_list), "числа(-ел)")

print(hat_list)


# Тут має бути Ваш код
# 1 реалізувати інтерактивне введення елементів масива
print("Добрий день. Давайте зберемо ваш масив")
userArray = []
while True:
    userInput = input("Додати число (щоб завершити введіть '.'): ")
    if userInput == '.':
        break
    elif userInput.isdigit() or (userInput[0] == '+' or '-') and userInput[1:].isdigit():
        userArray.append(int(userInput))
    else:
        print("Схоже ви ввели не число. Спробуйте ще раз")
print("Тож ваш масив до сортування виглядає наступним чином:", userArray)
# 2 оптимізувати процедуру сортування
changed = True
while changed:
    changed = False
    for num in range(len(userArray) - 1):
        if userArray[num] > userArray[num + 1]:
            userArray[num], userArray[num + 1] = userArray[num + 1],userArray[num]
            changed = True
print("Масив після сортування:", userArray)


my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Write your code here.
bufferList = []
for item in my_list:
    if item not in bufferList:
        bufferList.append(item)
my_list = bufferList[:]
#
print("The list with unique elements only:")
print(my_list)


chessboard = [['_' for i in range(8)] for j in range(8)]

for i in range(0,len(chessboard),len(chessboard) - 1):
    for j in range(0,len(chessboard[:]),len(chessboard[:]) - 1):
        chessboard[i][j] = 'П'

for row in chessboard:
    print(*row, sep='  ')