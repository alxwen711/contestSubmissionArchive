import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    x = input()
    #try 00/50 or 25/75
    ansa,ansb = -2,-2
    s = len(x)
    f = True
    for j in range(s):
        ansa += 1
        if f:
            if x[-1-j] == "0":
                f = False
        else:
            if x[-1-j] == "5" or x[-1-j] == "0": break
    f = True
    for k in range(s):
        ansb += 1
        if f:
            if x[-1-k] == "5":
                f = False
        else:
            if x[-1-k] == "2" or x[-1-k] == "7": break
    print(min(ansa,ansb))
    
