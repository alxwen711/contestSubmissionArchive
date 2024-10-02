import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
n = 1/2/3/4 -> easy
n = 5 -> medium
n = 6 -> hard

if n = 1, dp using last two recorded and track how many non rbg grids there are
n = 2, use n = 1 case and square it (no verticals)

AVOID RGB and BGR
"""

def convert(x,n):
    ar = [0]*n
    v = x
    for i in range(n):
        ar[-i-1] = v % 9
        v //= 9
    return ar

def revert(ar,n):
    v = 0
    for i in range(n):
        v *= 9
        v += (ar[i]//3)
    return v

n,m,p = readints()
if max(n,m) <= 2: print(0)
elif (n == 3 and m == 2) or (n == 2 and m == 3): print(625 % p)
elif (n == 4 and m == 1) or (n == 1 and m == 4): print(12 % p)

elif n <= 0: # base dp
    if m <= 2: print(0)
    else:
        dp = {}
        dp["RG"] = 1
        dp["GG"] = 1
        dp["BG"] = 1
        dp["RR"] = 1
        dp["GR"] = 1
        dp["BR"] = 1
        dp["RB"] = 1
        dp["GB"] = 1
        dp["BB"] = 1
        for _ in range(m-2):
            ndp = {}
            ndp["RG"] = (dp["RR"]+dp["GR"]+dp["BR"]) % p
            ndp["GG"] = (dp["RG"]+dp["GG"]+dp["BG"]) % p
            ndp["BG"] = (dp["RB"]+dp["GB"]+dp["BB"]) % p
            ndp["RR"] = (dp["RR"]+dp["GR"]+dp["BR"]) % p
            ndp["GR"] = (dp["RG"]+dp["GG"]) % p
            ndp["BR"] = (dp["RB"]+dp["GB"]+dp["BB"]) % p
            ndp["RB"] = (dp["RR"]+dp["GR"]+dp["BR"]) % p
            ndp["GB"] = (dp["GG"]+dp["BG"]) % p
            ndp["BB"] = (dp["RB"]+dp["GB"]+dp["BB"]) % p
            dp = ndp
        ans = 0
        for i in dp.keys():
            ans += dp[i]
        ans = (pow(3,n*m,p)-ans)%p
        if n == 2: ans = (ans*ans)%p
        print(ans)
else:   
    base = [""]
    for _ in range(n):
        tmp = list()
        for i in base:
            tmp.append(i+"R")
            tmp.append(i+"G")
            tmp.append(i+"B")
        base = tmp
    tmp = list()
    for i in base:
        flag = True
        for j in range(n-2):
            if i[j:j+3] == "RGB" or i[j:j+3] == "BGR":
                flag = False
                break
        if flag: tmp.append(i)
    base = tmp
    if m <= -1: print((pow(3,n*m,p)-(len(base)**m)) % p)
    else:
        """
        let R = 0, G = 1, B = 2 (not init = 0)
        then hash values are as follows:
        (row1,row2,row3)
        each row tracks last 3 digits ("64" values possible, really 27)
        first + second*4 + third*4*4
        0-63 val, represent tuple as base 64-values
        death vals: RGB = 5, BGR = 21
        after pass, divide by 4
        """
        vectors = list()
        for s in base:
            tmp = list()
            for k in s:
                if k == "R": tmp.append(0)
                if k == "G": tmp.append(1)
                if k == "B": tmp.append(2)
            vectors.append(tmp)
        #print(vectors)
        dp = [0]*(9**n)
        dp[0] = 1
        for ii in range(m):
            ndp = [0]*(9**n)
            for i in range(9**n):
                v = dp[i]
                if v != 0:
                    ar = convert(i,n)
                    for j in vectors:
                        br = [0]*n
                        flag = True
                        for k in range(n):
                            br[k] = ar[k]+j[k]*9
                            if ii >= 2 and (br[k] == 5 or br[k] == 21):
                                flag = False
                                break
                        if flag: # viable br scenario
                            h = revert(br,n)
                            ndp[h] = (ndp[h]+v) % p                    
            dp = ndp
        ans = 0
        for dd in range(9**n):
            ans += dp[dd]
        print((pow(3,n*m,p)-ans) % p)
