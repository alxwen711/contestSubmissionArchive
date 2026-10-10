import sys
from random import randint
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

def take_exam():
    prev = "."
    for _ in range(100):
        r = randint(1,448)
        if r % 2 == 0:
            prev = "T"
        else:
            prev = "F"
        print(prev)
        flush()
        ans = readin()
        if ans == "T": print("F")
        else: print("T")
        flush()
        ans = readin()
    return

for _ in range(readint()):
    take_exam()
