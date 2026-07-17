import sys

class Node:
   def __init__(self, val=None):
      self.val = val
      self.next = None

def bs(ar,val):
    high = len(ar)-1
    low = 0
    if high == -1: return 0
    while high-low > 1:
        mid = (low+high)//2
        if ar[mid] >= val: high = mid
        else: low = mid
    if ar[high] < val: return high+1
    elif ar[low] > val: return low
    return high

for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ar = list(map(int,sys.stdin.readline().split()))
    ar.sort()
    m = max(ar)
    """head = Node(ar[0])
    tmp = head
    for k in range(n-1):
        tmp.next = Node(ar[k+1])
        tmp = tmp.next
    while head != None:
        print(head.val)
        head = head.next
    """
    ans = "YES"
    for j in range(n-1):
        if ar[1]-ar[0] > 1:
            ans = "NO"
            break
        val = ar[1] + ar[0]
        ar.pop(0)
        ar.pop(0)
        ar.insert(bs(ar,val),val)
    if m <= 2: ans = "YES"
    print (ans)
    print(ar)
        

