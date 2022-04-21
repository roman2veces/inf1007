from chars_count import *

def get_numbers_in_file(file):
    with open(file, "r") as file_1:
        count = chars_count(file=file_1)
        char_index = 0
        numbers = []
        while char_index <= count:
            char = file_1.read(1)
            if char.isdigit():
                is_number = True
                while is_number:
                    next_char = file_1.read(1)
                    if next_char.isdigit():
                        char += next_char
                    else:
                        is_number = False
                numbers.append(int(char))
            char_index += 1
        numbers.sort()
    return numbers

print(get_numbers_in_file("text_with_numbers.txt"))
