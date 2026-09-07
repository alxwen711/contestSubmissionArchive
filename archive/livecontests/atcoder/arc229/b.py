import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
solve right to left (determine min/max cases

5 4 3 2 1 is impossible, min setup is 16 8 4 2 1
max setup (for 1 op) is 31 15 7 3 1


20 10 1 -> 14 7 0 (full subtract would break this)
20 10 1 -> 13 7 0 under binary search (NO)
condition is to subtract as much as possible with the rule
that next value must be at least twice the previous

are we sure we can't just binary search over largest possible?
then do some sort of multiplicativaty

1
2-3
4-7
8-15

8 5 2 1 is impossible

create some sort of upper limiter, then do the subtraction passthrough
if the previous value is EXACTLY double, then can NEVER do 2x+1

actually just check that part of the condition first
"""

for _ in range(readint()):
    n = readint()
    ar = readar()
    ans = 0
    flag = True
    for i in range(n-1):
        if ar[i+1]*2 > ar[i]:
            flag = False
            break
    if not flag: print(-1)
    else:
        for i in range(n-1,-1,-1):
            if ar[i] != 0:
                if i != n-1: # must subtract one at a time
                    ans += ar[i]
                    diff = ar[i]
                    # determine how big the base subtraction could be
                    minsub = ar[i]*2
                    maxsub = ar[i]*2+diff
                    ar[i] = 0
                    for j in range(i-1,-1,-1):
                        if maxsub <= ar[j]:
                            if (ar[j]-maxsub) >= ar[j+1]*2:
                                ar[j] -= maxsub
                                minsub = maxsub*2
                                maxsub = minsub+diff
                            else:
                                adjust = ar[j]-ar[j+1]*2
                                ar[j] -= (adjust)
                                minsub = adjust*2-2
                                maxsub = minsub+diff
                        else:
                            minsub = ar[j]*2
                            maxsub = ar[j]*2+diff
                            ar[j] = 0
                else:
                    ans += 1 # can full subtract this
                    # determine how big the base subtraction could be
                    minsub = ar[i]*2
                    maxsub = ar[i]*2+1
                    ar[i] = 0
                    for j in range(i-1,-1,-1):
                        if maxsub <= ar[j]:
                            if (ar[j]-maxsub) >= ar[j+1]*2:
                                ar[j] -= maxsub
                                minsub = maxsub*2
                                maxsub = minsub+1
                            else:
                                ar[j] -= (maxsub-1)
                                minsub = maxsub*2-2
                                maxsub = minsub+1
                        else:
                            minsub = ar[j]*2
                            maxsub = ar[j]*2+1
                            ar[j] = 0
            #print(ar,ans)
        print(ans)

                    

