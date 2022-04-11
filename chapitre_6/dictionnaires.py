dic = { n: n * 10 for n in range(10) }

for element in dic:
    print(element, dic[element])

# Montrer que les dictionnaires font de references
dicShallowCopy = dic    
dicShallowCopy[1] = 27
print(dicShallowCopy)
print(dic)

# Enlever la references avec deepCopy
dicDeepCopy = dic.copy()
dicDeepCopy[1] = 50
print(dicDeepCopy)
print(dic)