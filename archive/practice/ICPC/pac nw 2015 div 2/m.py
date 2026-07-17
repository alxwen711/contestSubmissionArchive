import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

ar = list()
for j in range(100):
    ar.append(j+1)

for i in range(readint()):
    a,b = map(str,sys.stdin.readline().split())
    b = int(b)
    for k in range(100):
        if ar[k] != -987654321:
            if a == "ADD": ar[k] += b
            elif a == "MULTIPLY": ar[k] *= b
            elif a == "SUBTRACT":
                ar[k] -= b
                if ar[k] < 0: ar[k] = -987654321
            else:
                if ar[k] % b != 0: ar[k] = -987654321
                else: ar[k] //= b
print(ar.count(-987654321))
