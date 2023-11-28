import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()


#python abuse lets go?

def solve(n):
    s = input()
    first = True
    q = 0
    r = 0
    if s[0] == "?":
        q += 1
        first = False
    else:
        r += int(s[0])
        
    for a in range(1,n):
        if s[a] == "?": q += 1
        else: r += int(s[a])

    if first:
        if r % 9 == 0: return "1"*(q-1)+"2"
        else: return "1"*q
    else:
        if r % 9 == 0: return "1"+"0"*(q-1)
        else: return "1"+"0"*(q-1)
        
for _ in range(readint()):
    print(solve(readint()))
