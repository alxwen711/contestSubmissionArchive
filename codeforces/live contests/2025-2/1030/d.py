import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
query count and n is at most 500 for easy part (graph setup?)
hard part is 200000
travel can be sped up to the next traffic light position
if a same red light positional is reached, infinite loop found
can use previous results to speed up queries
"""


for _ in range(readint()):
    n,k = readints()
    ar = readar()
    br = readar()
    q = readint()
    cr = readar()
    win = {}
    lose = {}
    for c in cr:
        if c > ar[-1]: print("YES")
        else:
            si = 0
            index = 0
            time = 0
            for i in range(n):
                if ar[i] >= c:
                    index = i
                    time = (ar[i]-c) % k
                    break
            right = True
            idk = {}
            while True:
                if time == br[index]: # redlight
                    kk = (index,time,right)
                    if win.get(kk) == 1:
                        print("YES")
                        for ii in idk.keys():
                            win[ii] = 1
                        break
                    if lose.get(kk) == 1:
                        print("NO")
                        for ii in idk.keys():
                            lose[ii] = 1
                        break
                    if idk.get(kk) == 1: # inf loop
                        print("NO")
                        for ii in idk.keys():
                            lose[ii] = 1
                        break
                    idk[kk] = 1
                    if right: right = False
                    else: right = True

                # greenlight
                if right:
                    if index == n-1:
                        print("YES")
                        for ii in idk.keys():
                            win[ii] = 1
                        break
                    else:
                        index += 1
                        time = (time+ar[index]-ar[index-1]) % k
                else:
                    if index == 0:
                        print("YES")
                        for ii in idk.keys():
                            win[ii] = 1
                        break
                    else:
                        index -= 1
                        time = (time+ar[index+1]-ar[index]) % k
                                        
