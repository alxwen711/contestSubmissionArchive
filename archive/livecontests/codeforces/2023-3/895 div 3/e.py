import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def create_sparse(ar: list) -> list:
    s = list()
    s.append(ar)
    prevrow = 0
    dist = 2 #length of subarray representation
    while dist <= len(ar):
        x = len(ar)-dist+1
        tmp = [0]*x
        for i in range(x):
            #find [i:i+dist]
            tmp[i] = s[prevrow][i] ^ s[prevrow][i+dist//2]
        s.append(tmp)
        prevrow += 1
        dist = dist << 1
    return s



def exact_query(l: int, h: int, ar: list):
    #default setting is to find minimum of subarray
    length = h-l+1
    s = str(bin(length))[2:]
    two = len(s)
    pt = l
    ans = 0
    for i in range(two):
        if s[i] == "1":
            ans ^= ar[two-i-1][pt]
            pt += 2**(two-i-1)
    return ans


for i in range(readint()):
    n = readint()
    ar = readar()
    s = sys.stdin.readline()
    br = list()
    cr = list()
    zero = 0
    one = 0
    for j in range(n):
        x = ar[j]
        if s[j] == "0":
            zero ^= x
            br.append(x)
            cr.append(0)
        else:
            one ^= x
            br.append(0)
            cr.append(x)
    bbr = create_sparse(br)
    ccr = create_sparse(cr)
    ans = list()
    for k in range(readint()):
        dr = readar()
        if dr[0] == 1:
            a,b = exact_query(dr[1]-1,dr[2]-1,bbr),exact_query(dr[1]-1,dr[2]-1,ccr)
            zero ^= a
            zero ^= b
            one ^= a
            one ^= b
        elif dr[1] == 0: ans.append(zero)
        else: ans.append(one)
    #print(bbr)
    #print(ccr)
    print(*ans)
