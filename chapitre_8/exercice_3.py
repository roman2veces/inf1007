def convert_note(note: int) -> str:
    if note < 10:
        return "F"
    elif note < 12:
        return "D"
    elif note < 14:
        return "C"
    elif note < 16:
        return "B"
    elif note < 18:
        return "A"
    elif note <= 20:
        return "A*"

with open("notes.txt", "r") as file_1, open("results_in_letter.txt", "w") as file_2:
    notes = [line.strip() for line in file_1.readlines()]
    lines_to_write = []
    for note in notes:
        line = f"{note} \t {convert_note(int(note))}"  
        lines_to_write.append(line)
        lines_to_write.append("\n")

    file_2.writelines(lines_to_write)
    

