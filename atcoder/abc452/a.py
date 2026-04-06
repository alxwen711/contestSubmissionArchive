import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

m,d = readints()
if m == 1 and d == 7: print("Yes")
elif m == 3 and d == 3: print("Yes")
elif m == 5 and d == 5: print("Yes")
elif m == 7 and d == 7: print("Yes")
elif m == 9 and d == 9: print("Yes")
else: print("No")
