import sys
import random
from copy import deepcopy

HMOD = 2147483647
HBASE1 = random.randrange(HMOD)
HBASE2 = random.randrange(HMOD)


class Hashing:
    def __init__(self, s, mod=HMOD, base1=HBASE1, base2=HBASE2):
        self.mod, self.base1, self.base2 = mod, base1, base2
        self._len = _len = len(s)
        f_hash, f_pow = [0] * (_len + 1), [1] * (_len + 1)
        s_hash, s_pow = f_hash[:], f_pow[:]
        for i in range(_len):
            f_hash[i + 1] = (base1 * f_hash[i] + s[i]) % mod
            s_hash[i + 1] = (base2 * s_hash[i] + s[i]) % mod
            f_pow[i + 1] = base1 * f_pow[i] % mod
            s_pow[i + 1] = base2 * s_pow[i] % mod
        self.f_hash, self.f_pow = f_hash, f_pow
        self.s_hash, self.s_pow = s_hash, s_pow

    def hashed(self, start, stop):
        return (
            (self.f_hash[stop] - self.f_pow[stop - start] * self.f_hash[start]) % self.mod,
            (self.s_hash[stop] - self.s_pow[stop - start] * self.s_hash[start]) % self.mod,
        )

    def get_hashes(self, length):
        return (
            [(self.f_hash[i + length] - self.f_pow[length] * self.f_hash[i]) % self.mod for i in range(self._len - length + 1)],
            [(self.s_hash[i + length] - self.s_pow[length] * self.s_hash[i]) % self.mod for i in range(self._len - length + 1)],
        )
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
any substring length k that isn't a palindrome makes it k-good
same letter -> 0
ababababababa -> 1,3,5,7,9 fails
abcbabcbabcba -> only 13 fails
ababababab -> 1,3,5,7,9 fails
track each pair of elements with min/max tracking
instant checkup of a string uses hashing

to anyone that is contemplating actually trying to hack me, I
have intentionally researched an actually hard to crack
hashing system specifically for this because I have been
screwed over SO many times before and I know at least one
person is half contemplating trying to here so don't even
bother.

"""

def create_sparse(br):
    ar = list()
    tmp = list()
    for i in br:
        tmp.append((i,i))
    ar.append(tmp)
    while len(ar[-1]) != 1:
        tmp = list()
        for j in range(len(ar[-1])//2):
            tmp.append((min(ar[-1][2*j][0],ar[-1][2*j+1][0]),max(ar[-1][2*j][1],ar[-1][2*j+1][1])))
        ar.append(tmp)
    return ar

def query(ar,l,r): # to fix
    if l > r: return -1
    # find sum between indicies 0 to x
    lp = l
    rp = r
    mn,mx = 99999999999999999999999,-9999999999999999999999999
    for i in range(len(ar)):
        if lp > rp: break
        if lp % 2 == 1:
            mn = min(mn,ar[i][lp][0])
            mx = max(mx,ar[i][lp][1])
            lp += 1
        if rp % 2 == 0:
            mn = min(mn,ar[i][rp][0])
            mx = max(mx,ar[i][rp][1])
            rp -= 1
        lp //= 2
        rp //= 2
    if mn == mx: return mx
    return -1

for _ in range(readint()):
    n,q = readints()
    s = sys.stdin.readline()[:n]
    ar = list()
    for snth in range(n):
        ar.append(ord(s[snth]))
    br = deepcopy(ar)
    br.reverse()
    fhash = Hashing(ar)
    bhash = Hashing(br)

    lb = list()
    for ii in range(n//2):
        lb.append((ord(s[ii*2])-97)*26+ord(s[ii*2+1])-97)
    pair = create_sparse(lb)
    ans = list()
    for i in range(q):
        l,r = readints()
        length = r-l+1 # always at least 2
        twoply = False
        v = -1
        if l % 2 == 1 and r % 2 == 0: # full pair set
            v = query(pair,l//2,r//2-1)
            if v != -1: twoply = True
        elif l % 2 == 0 and r % 2 == 1: # split in then full pair
            if l+1 == r: #edge 2 case
                if s[l-1] == s[r-1]:
                    twoply = True
                    v = 27
            else:
                v = query(pair,l//2,r//2-1)
                if (v != -1) and (s[l-1] == s[l+1]) and (s[r-1] == s[r-3]): twoply = True    
                
        elif l % 2 == 1 and r % 2 == 1: # check first with last, start on first
            v = query(pair,l//2,r//2-1)
            if v != -1 and s[l-1] == s[r-1]: twoply = True
        else: # check last with first, start on second
            v = query(pair,l//2,r//2-1)
            if v != -1 and s[l-1] == s[r-1]: twoply = True
        if twoply and v % 27 == 0: ans.append(0)
        elif twoply:
            lv = length//2
            ans.append((lv+1)*(lv)) #only even values
        elif fhash.hashed(l-1,l-1+(length//2)) == bhash.hashed(n-r,n-r+(length//2)): ans.append(((length-1)*(length))//2-1) #check if entire is palindrome
        else: ans.append(((length+1)*(length))//2-1) #full set -1

    for a in ans:
        print(a)
