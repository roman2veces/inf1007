def chars_count(file) -> int:
    lines = file.readlines()
    count = 0 
    for line in lines:
        count += len(line)

    file.seek(0)
    return count