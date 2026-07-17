import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def solve(s):
    l = 0
    slim = 0 #number of confirmed sorted values
    uslim = -1 #number of confirmed unsorted values
    for x in s:
        if x == "+": l += 1
        elif x == "-":
            l -= 1
            if l < 0: return "NO" #negative length
            if slim > l:
                slim -= 1
            if uslim > l:
                uslim = -1
        else:
            a = slim
            b = uslim
            if x == "1": #sorted?
                if uslim != -1: return "NO" #unsorted prefix
                slim = l
            else: #unsorted?
                if l < 2: return "NO" #too short
                if a == l: return "NO"
                if uslim == -1: uslim = l
    return "YES"

for i in range(readint()):
    s = sys.stdin.readline()[:-1]
    print(solve(s))
