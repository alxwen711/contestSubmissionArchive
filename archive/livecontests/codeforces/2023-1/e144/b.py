import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()


def dup(a,b):
    aa,bb = len(a),len(b)
    if aa == 1 or bb == 1: return -1
    h = [0]*676
    for i in range(aa-1):
        h[((ord(a[i])-97)*26)+ord(a[i+1])-97] = 1
    for j in range(bb-1):
        v = ((ord(b[j])-97)*26)+ord(b[j+1])-97
        if h[v] == 1: return v
    return -1
    
for i in range(readint()):
    a = sys.stdin.readline()[:-1]
    b = sys.stdin.readline()[:-1]
    if a[0] == b[0]:
        print("YES")
        print(a[0]+"*")
    elif a[-1] == b[-1]:
        print("YES")
        print("*"+a[-1])
    else:
        x = dup(a,b)
        if x == -1: print("NO")
        else:
            print("YES")
            print("*"+chr((x//26)+97)+chr((x%26)+97)+"*")
    
