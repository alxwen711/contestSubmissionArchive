import sys
import random

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
it's possible to use hash system to determine if certain part
is a palindrome in basically O(1) time

any sort of single char setup -> autofail
if current length is even pal -> split into disjoint halves

in case of emergency, break glass, glass being the hashing algo
"""

def notp(front,back,a,b,n):
    return front.hashed(a,b) != back.hashed(n-1-b,n-1-a)

for _ in range(readint()):
    s = sys.stdin.readline()[:-1]
    ar = list()
    br = list()
    for i in s:
        ar.append(ord(i))
        br.append(ord(i))
    front = Hashing(ar)
    br.reverse()
    back = Hashing(br)
    #ar.reverse()
    n = len(ar)
    if notp(front,back,0,n-1,n): # no break
        print("YES")
        print(1)
        print(s)
    else:
        index = -1
        for i in range(2,n-1):
            #print(i)
            if notp(front,back,0,i-1,n) and notp(front,back,i,n-1,n):
                index = i
                break
        if index == -1: print("NO")
        else:
            print("YES")
            print(2)
            print(s[:index],s[index:])

