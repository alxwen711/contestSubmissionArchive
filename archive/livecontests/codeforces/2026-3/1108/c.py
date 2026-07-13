import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
the array is non decreasing
there is a certain point where if the absolute value is not 0
but less than the absolute value of current value, impossible

there appears to be far fewer actual states to track than expected
"""
mod = 1000000007

for _ in range(readint()):
    n = readint()
    ar = readar()
    dpinc = {}
    dpdec = {}
    dpinc[0] = 1
    for i in ar:
        ndpinc = {}
        ndpdec = {}
        for a in dpinc.keys():
            v = a+i
            if (abs(v) >= abs(i)) or (v == 0) or (a >= 0):
                if ndpdec.get(v) == None: ndpdec[v] = 0
                ndpdec[v] = (ndpdec[v] + dpinc[a]) % mod
            #if abs(a) >= abs(i) or a == 0:
            if ndpinc.get(a) == None: ndpinc[a] = 0
            ndpinc[a] = (ndpinc[a] + dpinc[a]) % mod
        for b in dpdec.keys():
            v = b-i
            if (abs(v) >= abs(i)) or (v == 0) or (b <= 0):
                if ndpinc.get(v) == None: ndpinc[v] = 0
                ndpinc[v] = (ndpinc[v] + dpdec[b]) % mod
            #if abs(b) >= abs(i) or b == 0:
            if ndpdec.get(b) == None: ndpdec[b] = 0
            ndpdec[b] = (ndpdec[b] + dpdec[b]) % mod
        dpinc = ndpinc
        dpdec = ndpdec
        #print(dpinc,dpdec)
    print((dpinc.get(0,0)+dpdec.get(0,0)) % mod)
