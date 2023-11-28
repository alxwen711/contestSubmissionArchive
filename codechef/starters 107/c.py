import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
must be both even num of 0s/1s
each gap of 1s/0s should be even? (this is not the case
11001010 -> 11111010 -> 11100010 -> 11101110
11101000 -> ?

100111000110 counterexample
(())()()(())
bracket idea: each 1st 1/0 -> (, 2nd 1/0 -> )
how to represent the 1010 interlocking?
coloured brackets (depends on 1/0 colour)
11001010
()()(())
no 101/010?
100010 fails (practically breaks into a 1010 case)
1010110101

stack operation

0010110100

if odd string can break into even-single-even
even can break into even-single-even-single-even?
this still results in stack setup working
0011100001111001
"""

def solve(n,ar):
    if n % 2 == 0:
        br = list()
        for i in ar:
            br.append(i)
            if len(br) >= 2:
                if br[-1] == br[-2]:
                    br.pop()
                    br.pop()
        if len(br) == 0: return "Yes"
        return "No"
    else:
        #odd case effectively splits into 2 even strings
        #calculate for each length two string l->r then r->l
        #dp check if any pair works
        
        lr = [0]*(n//2+1)
        lr[0] = 1
        br = list()
        for i in range(n//2):
            br.append(ar[i*2])
            if len(br) >= 2:
                if br[-1] == br[-2]:
                    br.pop()
                    br.pop()
            br.append(ar[i*2+1])
            if len(br) >= 2:
                if br[-1] == br[-2]:
                    br.pop()
                    br.pop()
            if len(br) == 0: lr[i+1] = 1
            
        rl = [0]*(n//2+1)
        rl[0] = 1
        for i in range(n//2):
            br.append(ar[-i*2-1])
            if len(br) >= 2:
                if br[-1] == br[-2]:
                    br.pop()
                    br.pop()
            br.append(ar[-i*2-2])
            if len(br) >= 2:
                if br[-1] == br[-2]:
                    br.pop()
                    br.pop()
            if len(br) == 0: lr[i+1] = 1

        for v in range(n//2+1):
            if lr[v] == 1 and rl[(n//2)-v] == 1: return "Yes"
        return "No"
    
for _ in range(readint()):
    n = readint()
    s = sys.stdin.readline()
    ar = list()
    for i in range(n):
        ar.append(int(s[i]))
    print(solve(n,ar))
