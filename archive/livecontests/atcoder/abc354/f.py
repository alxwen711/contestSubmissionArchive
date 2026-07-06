import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
LIS on its own is n log n to get LIS length

everything on a maximal length will pass
"""

def bsearch(x,longest):
    low = 0
    high = len(longest)-1
    if high-low > 1:
        mid = (low+high)//2
        if longest[mid][-1][0] >= x: high = mid
        else: low = mid
    if longest[low][-1][0] >= x: return low
    if longest[high][-1][0] >= x: return high
    return high+1

for _ in range(readint()):
    n = readint()
    ar = readar()
    longest = list()
    longest.append([(ar[0],0)])
    for i in range(1,n):
        index = bsearch(ar[i],longest)
        if index == len(longest): longest.append([(ar[i],i)])
        else: longest[index].append((ar[i],i))
    #print(longest)

    # determine all used values from this point on
    h = [0]*n
    longest.reverse()
    for ai in longest[0]:
        h[ai[1]] = 1
    for a in range(1,len(longest)):
        index = len(longest[a-1])-1
        for b in range(len(longest[a])):
            # compare longest[a][-b-1] and longest[a-1][index]
            #if longest[a][-b-1][0] < longest[a-1][index][0] and longest[a][-b-1][1] < longest[a-1][index][1]:
            for c in range(len(longest[a-1])):
                if h[longest[a-1][c][1]] == 1 and longest[a][-b-1][1] < longest[a-1][c][1] and longest[a][-b-1][0] < longest[a-1][c][0]:
                    h[longest[a][-b-1][1]] = 1
                    break
            """
            while True:
                if index == -1: break
                elif h[longest[a-1][index][1]] == 0: index -= 1
                elif longest[a][-b-1][0] >= longest[a-1][index][0]: index -= 1
                elif longest[a][-b-1][1] >= longest[a-1][index][1]: break
                else:
                    h[longest[a][-b-1][1]] = 1
                    break
            """
    #print(h)
    ans = list()
    for ii in range(n):
        if h[ii]: ans.append(ii+1)
    print(len(ans))
    print(*ans)
