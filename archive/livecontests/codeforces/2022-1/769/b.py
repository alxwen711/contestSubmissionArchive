import sys
for i in range(int(sys.stdin.readline())):
    x = int(sys.stdin.readline())
    if x == 0: print("0")
    elif x == 1: print("0 1")
    else:
        #a = list()
        e = 2
        while e*2 < x:
            e = e*2
        for j in range(x-e):
            print(x-j-1, end=" ")

        for k in range(e):
            print(k, end=" ")
        print()
