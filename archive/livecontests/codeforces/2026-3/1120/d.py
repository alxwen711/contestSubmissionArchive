import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
permutation indicates that the order the sorcerers are removed
can be arbritary

possibly start from the reverse case of 1 sorcerer and add?
in this case number of forfeits will only ever increase by 1 each time
or if someone ridiculously strong is inserted earlier on then
it could remove a lot

NOTE: if not beating champion, still could contribute enough
strength to disrupt later order
"""

def create_seg(n):
    seg = list()
    tmp = [0]*n
    seg.append(tmp)
    vv = len(seg[-1])
    while vv > 1:
        vv >>= 1
        tmp = [0]*vv
        seg.append(tmp)
    return seg

def update_seg(seg,index,val):
    i = index
    for j in range(len(seg)):
        if len(seg[j]) == i: break
        seg[j][i] += val
        i >>= 1

def query(seg,li,ri):
    l,r = li,ri
    ans = 0
    for i in range(len(seg)):
        if l > r: break
        if l % 2 == 1:
            ans += seg[i][l]
            l += 1
        if r % 2 == 0:
            ans += seg[i][r]
            r -= 1
        l >>= 1
        r >>= 1
    return ans

def find_previous_champ(seg,index):
    if index == 0: return -1
    low = 0
    high = index-1
    while high-low > 1:
        mid = (low+high) >> 1
        if query(seg,mid,index-1): low = mid
        else: high = mid
    if query(seg,high,index-1): return high
    if query(seg,low,index-1): return low
    return -1

def find_next_champ(seg,index,snth):
    if index == snth: return -1
    low = index+1
    high = snth
    while high-low > 1:
        mid = (low+high) >> 1
        if query(seg,index+1,mid): high = mid
        else: low = mid
    if query(seg,index+1,low): return low
    if query(seg,index+1,high): return high
    return -1

anslist = list()

for _ in range(readint()):
    n = readint()
    ar = readar()
    br = readar() # permutation, treat this in reverse for sorcs getting added
    ans = [0]*n
    sum_seg = create_seg(n)
    champ_seg = create_seg(n)
    prev_champ = [-1]*n
    next_champ = [-1]*n
    ca = -1
    for i in range(n-1,-1,-1):
        index = br[i]-1 # index in whatever ds to add to
        val = ar[index] # strength to add
        update_seg(sum_seg,index,val)
        if ca == -1: # automatically assign champion
            ca += 1
            update_seg(champ_seg,index,1)
        else: # check if this is a new champion or gets beat by previous
            pchamp = find_previous_champ(champ_seg,index)
            newchamp = False
            if pchamp == -1:
                newchamp = True # first in line
                nchamp = find_next_champ(champ_seg,index,n-1)
                next_champ[index] = nchamp
                prev_champ[nchamp] = index
            else:
                ps = ar[pchamp]+query(sum_seg,pchamp+1,index-1)
                if ps < val: # there would be a new champ here
                    newchamp = True
                    nchamp = find_next_champ(champ_seg,index,n-1)
                    next_champ[index] = nchamp
                    prev_champ[nchamp] = index
                    prev_champ[index] = pchamp
                    next_champ[pchamp] = index
            if newchamp:
                ca += 1
                update_seg(champ_seg,index,1)
                nchamp = next_champ[index]
                while nchamp != -1:
                    strength = val+query(sum_seg,index+1,nchamp-1)
                    if strength >= ar[nchamp]: # overtake
                        ca -= 1
                        update_seg(champ_seg,nchamp,-1)
                        next_champ[index] = next_champ[next_champ[index]]
                        prev_champ[nchamp] = -1
                        next_champ[nchamp] = -1
                        if next_champ[index] != -1:
                            prev_champ[next_champ[index]] = index
                        nchamp = next_champ[index]
                    else: break
            else: # recheck pchamp
                nchamp = next_champ[pchamp]
                while nchamp != -1:
                    strength = ar[pchamp]+query(sum_seg,pchamp+1,nchamp-1)
                    if strength >= ar[nchamp]: # overtake
                        ca -= 1
                        update_seg(champ_seg,nchamp,-1)
                        next_champ[pchamp] = next_champ[next_champ[pchamp]]
                        prev_champ[nchamp] = -1
                        next_champ[nchamp] = -1
                        if next_champ[pchamp] != -1:
                            prev_champ[next_champ[pchamp]] = pchamp
                        nchamp = next_champ[pchamp]
                    else: break
        ans[i] = ca
    anslist.append(" ".join(map(str,ans)))
sys.stdout.write("\n".join(anslist))

    
