from random import shuffle
ar = list()
for i in range(48):
    ar.append(0)
    ar.append(1)
ar.append(1)
shuffle(ar)
print(*ar,sep="")
