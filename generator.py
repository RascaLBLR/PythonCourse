def generator():
    for x in range (1, 11):
        if x % 3 == 0:
            yield print("Вася!!!")
        else:
            yield print(x)
        
nmbr = generator()
for i in range (10):
    next(nmbr)

