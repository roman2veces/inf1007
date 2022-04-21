with open("test1", "r") as file_1, open("test2", "r") as file_2:
    lines = file_1.readlines()
    char_count = 0 
    for line in lines:
        char_count += len(line)

    current_char = 0 
    no_difference = True
    file_1.seek(0)
    while (current_char <= char_count) and no_difference:
        char_1 = file_1.read(1)
        char_2 = file_2.read(1)
        if char_1 != char_2:
            print(f"First difference: {char_1} != {char_2}")
            print(current_char)
            no_difference = False
        current_char += 1

    if no_difference:
        print("Same content in both files")
