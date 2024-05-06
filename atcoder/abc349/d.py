import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
jump by some exponent of 2
go to closest exponent of 2 allowed
"""
l,r = readints()
ans = list()
pos = l
while pos != r:
    base = 1
    while True:
        base *= 2
        if pos % base != 0 or pos+base > r:
            base //= 2
            break
    ans.append((pos,pos+base))
    pos += base
print(len(ans))
for i in ans:
    print(i[0],i[1])
