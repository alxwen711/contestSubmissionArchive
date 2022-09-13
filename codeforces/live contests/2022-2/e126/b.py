#32768 = 2**15 (1000 0000 0000 0000)
"""
10011 (score = 15)
10100 (score = 13)
"""
import sys

def b(j):
    x = j
    ans = 15
    while ans != 0:
        if x % 2 == 1: return ans
        ans -= 1
        x = x // 2
    return ans


n = int(sys.stdin.readline())
ar = list(map(int,sys.stdin.readline().split()))
for i in range(len(ar)):
    num = ar[i]
    h = [99]*16
    for j in range(16):
        h[j] = b(num+j)+j
        if num+j == 32768: break
    print(min(h),end=" ")
