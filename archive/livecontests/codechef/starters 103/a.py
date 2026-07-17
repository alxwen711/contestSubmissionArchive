import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    a,s = map(str,sys.stdin.readline().split())
    n = len(s)
    if n == 1: print(8)
    elif n == 2:
        if int(s) % 8 == 0: print(s)
        else:
            st = int(s[0])*10
            while st % 8 != 0:
                st += 1
            print(st)
    else:
        l = int(s[-3:])
        if l % 8 == 0: print(s)
        else:
            st = int(l)//10*10
            while st % 8 != 0:
                st += 1
            st = str(st)
            while len(st) != 3:
                st = "0"+st
            print(s[:-3]+st)
        
