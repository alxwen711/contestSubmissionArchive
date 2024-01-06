import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
later consider multiple z
SUBSEQUENCE
czddeneeeemigec (znmigec)
ccddezeeeenmige (znmige)
ccddeeeeeeznmig
ccddeeeeeegznmi
"""

def stringsorted(ar):
    for i in range(len(ar)-1):
        if ord(ar[i]) > ord(ar[i+1]): return False
    return True


for _ in range(readint()):
    n = readint()
    s = sys.stdin.readline()[:-1]
    ar = list()
    for ii in range(n):
        ar.append(s[ii])
    if stringsorted(ar): print(0)
    else:
        subseq = list()
        for i in range(n):
            ch = ar[i]
            while len(subseq) != 0:
                if ord(ch) > ord(subseq[-1][0]): subseq.pop()
                else: break
            subseq.append((ch,i))
        for j in range(len(subseq)):
            ar[subseq[j][1]] = subseq[-j-1][0]
        if stringsorted(ar):
            ans = len(subseq)
            first = subseq[0][0]
            for k in range(len(subseq)):
                if subseq[k][0] == first: ans -= 1
                else: break
            print(ans)
        else: print(-1)
