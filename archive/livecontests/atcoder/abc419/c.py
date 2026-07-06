import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())
mia,maa,mib,mab = 9999999999999999999,-9999999999999999999,9999999999999999999,-9999999999999999999
for _ in range(readint()):
    a,b = readints()
    mia = min(mia,a)
    mib = min(mib,b)
    maa = max(maa,a)
    mab = max(mab,b)
print(max((mab-mib+1)//2,(maa-mia+1)//2))
