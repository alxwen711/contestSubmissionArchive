import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

#undo operation is complicated
ans = 0
h = [0]*1000001
ar = list()

for i in range(readint()):
    s = list(map(str,sys.stdin.readline().split()))
    #flush() #for hard version
    if s[0] == "?": print(ans)
    
