import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
if everything is 0 this is towers of hanoi
is this actually bfs able?

if the number is not high enough, treat it as an individual hanoi problem??

0 1 1 is treated like 1-1 disks?

0 1 0 0 is treated like 2-1-1 disks
0 1 2 0 is treated like 3-1 disks
0 1 1 0 is treated like two-one disks
0 1 1 1 is treated like 1-1-1 disks?

maybe this is just brute force???
move the lowest one first every time?

greedily moving the disks as far right as possible does not work on 0,0,0,0 case

- construct the initial towers of hanoi solution
- maybe the numbers just let us skip various parts of the recursive iteration?
"""

def state:
    def __init__(self,st,pm = None):
        self.prevmove = pm
        self.one = list()
        self.two = list()
        self.three = list()
        for i in range(len(st)-1,-1):
            if st[i] == "1":
                self.one.append(i+1)
            elif st[i] == "2":
                self.two.append(i+1)
            else:
                self.three.append(i+1)
            
    def encode(self,n):
        hel = [" "]*n
        for a in self.one:
            hel[a-1] = "1"
        for b in self.two:
            hel[b-1] = "2"
        for c in self.three:
            hel[c-1] = "3"
        return "".join(hel)

def movelist(n,ar,s):
    ml = list()
    la,lb,lc = len(s.one),len(s.two),len(s.three)
    for a in range(la):
        if ar[s.one[a]-1] == la-a-1:
            # move a to b or c
            if lc == 0 or s.one[a] < s.three[0]:
                ml.append((s.one[a],1,3))
            if lb == 0 or s.one[a] < s.two[0]:
                ml.append((s.one[a],1,2))
            

for _ in range(readint()):
    n = readint()
    ar = readar()
    
    
