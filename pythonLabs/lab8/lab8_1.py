# считываем файл построчно
with open('input.txt', 'r') as f:
    lines = f.readlines()

# шифруем каждую строку
for i in range(len(lines)):
    shifted_line = ""
    for char in lines[i]:
        if char.isalpha():
            # определяем сдвиг для текущего символа
            shift = ord(char.lower()) - ord('a') + i + 1
            # выполняем циклический сдвиг
            shifted_char = chr((ord(char.lower()) - ord('a') + shift))
            # сохраняем регистр символа
            if char.isupper():
                shifted_char = shifted_char.upper()
            shifted_line += shifted_char
        else:
            shifted_line += char
    print(shifted_line, end="") # выводим шифрованную строку без перевода строки