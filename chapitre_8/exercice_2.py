from chars_count import *

with open("test1", "r") as file_1, open("3_spaces", "w") as file_2:
    count = chars_count(file=file_1)
    char_index = 0
    while char_index <= count:
        char = file_1.read(1)
        if char == " ":
            file_2.write("   ")
        else:
            file_2.write(char)
        char_index += 1
        
    
