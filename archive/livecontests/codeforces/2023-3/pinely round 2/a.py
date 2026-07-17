import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()



def test(n,a,q,s):
    x = a
    for i in range(q):
        if s[i] == "+": x += 1
        else: x -= 1
        if x == n: return True
    return False

for i in range(readint()):
    n,a,q = readints()
    s = input()
    if n == a: print("YES")
    else:
        if test(n,a,q,s): print("YES")
        else:
            if s.count("+")+a >= n: print("MAYBE")
            else: print("NO")
