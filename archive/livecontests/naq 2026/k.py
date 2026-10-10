import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

numbers = list()
for i in range(1,10):
    for j in range(1,11-i):
        v = 0
        d = j
        for k in range(i):
            v *= 10
            v += d
            d += 1
        numbers.append(v)
numbers.sort()
m = len(numbers)
for _ in range(readint()):
    n = readint()
    low = 0
    high = m-1
    while high-low > 1:
        mid = (low+high)//2
        if numbers[mid] >= n: high = mid
        else: low = mid
    if numbers[low] >= n: print(numbers[low])
    else: print(numbers[high])
