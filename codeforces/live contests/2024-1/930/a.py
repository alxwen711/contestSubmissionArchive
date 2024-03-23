import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
maximum is highest power of 2 present to get bin val 111...111

find power of two by comparing pairs, highest pair stays
+1 query between two values in highest pair, higher one MUST contain
the most significant bit and can make best value

brute force with this value across n steps, getting ALL values
that create the maximum OR. Then find the minimum of these values
to get maximum XOR.

"""

def solve():
    n = readint()
    if n == 2:
        print("! 0 1",flush=True)
        return
    ha,hb = 0,1
    for i in range((n-2)//2):
        s = "? "+str(ha)+" "+str(hb)+" "+str(2*i+2)+" "+str(2*i+3)
        print(s,flush=True)
        r = sys.stdin.readline()
        if r[0] == "<": #change
            ha,hb = 2*i+2,2*i+3

    if n % 2 == 1:
        s = "? "+str(ha)+" "+str(hb)+" "+str(n-1)+" "+str(n-1)
        print(s,flush=True)
        r = sys.stdin.readline()
        if r[0] == "<": #change
            ha,hb = n-1,n-1

    v1 = ha
    s = "? "+str(ha)+" "+str(ha)+" "+str(hb)+" "+str(hb)
    print(s,flush=True)
    r = sys.stdin.readline()
    if r[0] == "<": #change
        v1 = hb

    v2 = list()
    v2.append(0)
    for j in range(1,n):
        s = "? "+str(v1)+" "+str(v2[0])+" "+str(v1)+" "+str(j)
        print(s,flush=True)
        r = sys.stdin.readline()
        if r[0] == "<": #change
            v2 = list()
            v2.append(j)
        elif r[0] == "=":
            v2.append(j)

    m = v2[0]
    if len(v2) != 1:
        for k in range(1,len(v2)):
            s = "? "+str(m)+" "+str(m)+" "+str(v2[k])+" "+str(v2[k])
            print(s,flush=True)
            r = sys.stdin.readline()
            if r[0] == ">": #change
                m = v2[k]
        
    s = "! "+str(v1)+" "+str(m)
    print(s,flush=True)


    
for _ in range(readint()):
    solve()
