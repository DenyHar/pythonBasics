def mysplit(string):
    list_split = []
    word = ""
    for char in string:
        if char == " ":
            if word:
                list_split.append(word)
            word = ""
        else:
            word += char
    if word:
        list_split.append(word)
    return list_split


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))

# Тут має бути Ваш код
# number_input = input('Введіть ціле число: ')
# number_list = [str(i) for i in range(0, 10)]
number_dict = {'1' : ('  #', '  #', '  #', '  #', '  #'),
               '2' : ('###', '  #', '###', '#  ', '###'),
               '3' : ('###', '  #', '###', '  #', '###'),
               '4' : ('# #', '# #', '###', '  #', '  #'),
               '5' : ('###', '#  ', '###', '  #', '###'),
               '6' : ('###', '#  ', '###', '# #', '###'),
               '7' : ('###', '  #', '  #', '  #', '  #'),
               '8' : ('###', '# #', '###', '# #', '###'),
               '9' : ('###', '# #', '###', '  #', '###'),
               '0' : ('###', '# #', '# #', '# #', '###')
               }
def display_number(num):
    if num < 0:
        print("Число має бути невід'ємним.")
        return

    num_str = str(num)

    for level in range(5):
        for simbol in num_str:
            print(number_dict[simbol][level], end=' ')
        print()

display_number(123)

# Caesar cipher.
text = input("Enter your message: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)

# Тут має бути Ваш код
# Caesar cipher - decrypting a message.
cipher = input('Enter your cryptogram: ')
text = ''
for char in cipher:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)

print(text)

# Тут має бути Ваш код
# Caesar cipher.
text = input("Введіть ваше повідомлення: ")
key = int(input("Введіть значення зсуву (1-25): "))
while True:
    if 0 < key < 26:
        break
    else: key = int(input("Значення не дійсне. Спробуйте ще раз: "))
cipher = ''
for char in text:
    if not char.isalpha():
        code = ord(char)
        cipher += chr(code)
        continue
    if 'a' <= char <= 'z':
        code = ord(char) + key
        if code > ord('z'):
            code = (code % ord('z')) + ord('a') - 1
        cipher += chr(code)
    else:
        code = ord(char) + key
        if code > ord('Z'):
            code = (code % ord('Z')) + ord('A') - 1
        cipher += chr(code)

print(cipher)