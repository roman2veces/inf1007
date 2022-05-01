import time

with open("test1", "a+") as file:
    file.write("\nwriting from file 1")
    
    time.sleep(60)

    file.seek(0)
    print(file.read())
    





