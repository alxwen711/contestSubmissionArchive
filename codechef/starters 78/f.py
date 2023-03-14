import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def fi(base,x):
    index = 0
    for i in range(len(base)):
        if base[i] < x: index += 1
        else: break
    return index

def f(n,s,k,base,ii):
    ls = len(s)
    if ii == ls: return 0
    if k == 1:
        g = int("1"*ls)*int(s[0])
        if n > g: g += int("1"*ls)
        return g-n
    ans = (-n) % (10**(ls-k+1))
    ar = [0]*ls
    for u in range(ls):
        ar[u] = int(s[u])
    over = False
    lb = len(base)
    for v in range(ii,ls):
        if over: ar[v] = base[0]
        else:
            x = ar[v]
            index = fi(base,x)
            if index != lb:
                ar[v] = base[index]
                if base[index] > x:
                    over = True
            else:
                bt = v-1
                while bt != -1: #with two digits there will be one eventually
                    vv = fi(base,ar[bt])
                    if vv != lb-1:
                        ar[bt] = base[vv+1]
                        for snth in range(bt+1,ls):
                            ar[snth] = base[0]
                        break
                    else: bt -= 1
                break
    lth = 0
    for why in range(ls):
        lth *= 10
        lth += ar[why]
    return min(ans,lth-n)


for i in range(readint()):
    h = [0]*10
    n,k = readints()
    s = str(n)
    a = 0
    index = 0
    for j in range(len(s)):
        index += 1
        if h[int(s[j])] == 0:
            a += 1
            h[int(s[j])] = 1
        if a == k: break
    base = list()
    for m in range(10):
        if h[m] == 1: base.append(m)
    print(f(n,s,k,base,index))
