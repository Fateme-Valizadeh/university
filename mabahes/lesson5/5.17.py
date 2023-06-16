def display_ascii_table():
    start_char = ord('!')
    end_char = ord('~')
    chars_per_line = 10

    for char_code in range(start_char, end_char + 1):
        print(chr(char_code), end=' ')

        if (char_code - start_char + 1) % chars_per_line == 0:
            print()

display_ascii_table()
