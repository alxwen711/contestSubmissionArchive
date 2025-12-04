import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
always use I where possible

II < IV

greedy rearrangement? (determine how many extra -1s could happen

I? case should be considered

determine specific positions x and v should go first to maximize the
-1 count

for each segment, if I? is the start, mark from the first ?
else mark from the second ?
"""
score = {"X":10,"V":5,"I":1}
for _ in range(readint()):
    n,q = readints()
    s = readin()
    blank = 0 # number of blank spots
    neg1,neg2,neg3,neg4 = 0,0,0,0
    base = 0 # base score
    chain = 0
    for i in range(n):
        if s[i] == "?":
            chain += 1
        else:
            if chain != 0:
                # resolve chain
                sp = i-chain
                ep = i-1
                blank += chain
                if chain == 1: # super edge case
                    lf,rf = False,False
                    if sp != 0:
                        if s[sp-1] == "I": lf = True
                    if (s[i] == "X" or s[i] == "V"): rf = True
                    if lf:
                        if rf: neg4 += 1
                        else: neg1 += 1
                    elif rf: neg3 += 1
                else:
                    if sp != 0:
                        if s[sp-1] == "I":
                            neg1 += 1
                            chain -= 1

                    if (s[i] == "X" or s[i] == "V"):
                        neg3 += 1
                        chain -= 1
                    
                    neg2 += chain//2
                
                chain = 0
            if i != n-1:
                if s[i] == "I" and (s[i+1] == "X" or s[i+1] == "V"): base -= 1
                else: base += score[s[i]]
            else: base += score[s[i]]
    if chain != 0: # resolve chain
        sp = n-chain
        ep = n-1
        blank += chain
        # no ?X position is possible
        if chain == 1:
            if sp != 0:
                if s[sp-1] == "I":
                    neg1 += 1
        else:            
            if sp != 0:
                if s[sp-1] == "I":
                    neg1 += 1
                    neg2 += (chain-1)//2
                else:
                    neg2 += chain//2
            else: neg2 += chain//2
                
    for _ in range(q):
        x,v,i = readints()
        rx,rv,ri = 0,0,blank
        if ri > i:
            rv = ri-i
            ri = i
            if rv > v:
                rx = rv-v
                rv = v
        #print(rx,rv,ri)
        
        emptyleft = blank

        ans = rx*10+rv*5+base

        not1 = rx+rv

        # fill in the neg1 sections with X/V
        fs = min(not1,neg1)
        ans -= 2*fs
        emptyleft -= fs
        not1 -= fs
        
        # fill in the neg3 sections with I
        fv = min(ri,neg3)
        ans -= fv
        emptyleft -= fv
        ri -= fv

        
        
        # fill in the neg2 sections with IX or IV
        fk = min(not1,ri,neg2)
        ans -= fk
        emptyleft -= (2*fk)
        ri -= fk
        not1 -= fk

        # fill in neg4 sections with anything, preferrably with x or v?
        ans -= 2*neg4
        
        # the rest should be filled in whatever
        ans += ri

        print(ans)
    #print(neg1,neg2,neg3)



        
