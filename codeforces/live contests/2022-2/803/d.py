import sys
"""
some sort of binary search method is needed?
"""

def solve():
    n = int(sys.stdin.readline())
    """
    choose first half of range, rounded down
    from position determine what values should be there
    for n = 9, first case is positions 1 to 4
    count number tracked
    if even, singular is in opposite track
    if odd, singular is in same track
    14 guesses at most required to drop to 1 value
    15th guess will always be ? x x returning x
    once the range reaches one, answer can be returned
    test array [8,5,4,3,2,9,7,1,6], ans = 7
    """
    low = 1
    high = n
    for i in range(14):
        mid = low + ((high-low)//2)
        print("?",low,mid,flush=True)
        #test range is low to mid
        ar = list(map(int,sys.stdin.readline().split()))
        h = [0]*(mid-low+1)
        for j in range(mid-low+1):
            if ar[j] > mid: break
            if ar[j] >= low: h[ar[j]-low] = 1
        #if even, check right, else check left
        if sum(h) % 2 == 0: low = mid + 1
        else: high = mid
        if low + 1 >= high: break #1 or 2 numbers left
    print("?",low,low,flush=True)
    ar = int(sys.stdin.readline())
    if ar == low: return low
    else: return high

for i in range(int(sys.stdin.readline())):
    x = "! "+str(solve())
    print(x,flush=True)
