from random import randint,seed

seed(25876729)
print(4000)
for j in range(4000):
    print("25 5")
    a = list()
    b = list()
    for i in range(25):
        a.append(chr(97+randint(0,9)))
        b.append(chr(97+randint(0,9)))
    
    print(*a,sep="")
    print(*b,sep="")

