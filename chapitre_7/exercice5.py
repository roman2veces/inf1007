def f(a, b):
    # a et b sont des entiers naturels non nuls
    if b==1: 
        return a
    return a + f(a, b-1)
print(f(3, 5))