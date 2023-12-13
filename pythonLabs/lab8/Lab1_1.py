with open('input.txt', 'r') as f_in, open('output.txt', 'w') as f_out:

    for i, line in enumerate(f_in):
        shift = i + 1
        encrypted_line = ''
        for char in line:
            if char.isalpha() and char.isascii() and char.islower():
                char_code = ord(char)
                new_char_code = (char_code - ord('a') + shift) % 26 + ord('a')
                new_char = chr(new_char_code)
            elif char.isalpha() and char.isascii() and char.isupper():
                char_code = ord(char)
                new_char_code = (char_code - ord('A') + shift) % 26 + ord('A')
                new_char = chr(new_char_code)
            else:
                new_char = char
            encrypted_line += new_char
        f_out.write(encrypted_line)
