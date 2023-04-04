import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n = readint()
    s = input()
    v = 999
    index = -1
    for j in range(n):
        x = ord(s[j])
        if x <= v:
            index = j
            v = x
    print(s[index]+s[:index]+s[index+1:])
