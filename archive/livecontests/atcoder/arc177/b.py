import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()


"""
01001010
AAAAAAA -> 11111110
BBBBBB -> 00000010
AAAAA -> 1111101
BBBB -> 0000101
AAB -> 01001010
"""
n = readint()
s = input()
ans = list()
state = "0"
for i in range(n):
    if s[-i-1] != state:
        state = s[-i-1]
        inc = "B"
        if state == "1": inc = "A"
        for _ in range(n-i):
            ans.append(inc)
print(len(ans))
print(*ans,sep="")
