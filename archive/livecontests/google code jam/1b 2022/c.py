import sys
from random import randint

def b(t):
    ans = 0
    for i in range(8):
        ans += (2**i)*int(t[-i-1])
    return ans

def s(x):
    a = ""
    for w in range(8):
        a = str(x%2) + a
        x = x//2
    return a
        

def solve():
    print("11111111",flush=True) #find number of 1s
    ones = int(sys.stdin.readline())
    if ones == 0: return 0
    p = list() #possibilities list
    for k in range(256):
        a = ""
        x = k
        for bruh in range(8):
            a += str(x%2)
            x = x//2
        if a.count("1") == ones: p.append(a)

    h = [0]*256
    vara = list()
        
    for j in range(299):
        #print(p)
        t = p[randint(0,len(p)-1)]
        print(t,flush=True)
        ones = int(sys.stdin.readline())
        if ones == 0: return 0
        elif ones == 8:
            print("11111111",flush=True)
            ones = int(sys.stdin.readline())
            return 0
        
        #find all possible outcomes
        vara.clear()
        for m in range(8):
            vara.append(b(str(t[m:]+t[:m])))

        for why in range(256):
            h[why] = 0
        
        for s in range(len(p)):
            inting = b(p[0])
            for ss in range(8):
                h[inting^(vara[ss])] = 1
            p.pop(0)
        #print(h)
        #print(ones)
        for c in range(256):
            if h[c] == 1:
                cc = c
                n = ""
                onecount = 0
                for w in range(8):
                    n = str(cc%2) + n
                    if cc % 2 == 1: onecount += 1
                    cc = cc//2
                #print(onecount)
                if onecount == ones:
                    p.append(n)
                    #print("appended n")
    return -1

for i in range(int(sys.stdin.readline())):
    if solve() == -1: break
