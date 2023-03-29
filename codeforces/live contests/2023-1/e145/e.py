import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
left point: max a, min b
right point: min a, max b
"""
class zone:
    def __init__(self,cap,a,b):
        self.cap = cap
        #left endpoint
        self.la = cap
        self.lb = 0
        if cap > a:
            self.la -= (cap-a)
            self.lb = cap-a
        #right endpoint
        self.ra = 0
        self.rb = 0
        if cap > b:
            self.rb -= (cap-b)
            self.ra = cap-b
        # dist from left most state
        self.lv = 0
        self.rv = self.la-self.ra
        #maximum vals
        self.mla = self.la
        self.mlb = self.lb
        self.mra = self.ra
        self.mrb = self.rb

    def move(self,x):
        # move x liters left to right
        self.la -= x
        self.lb += x
        self.ra -= x
        self.rb += x
        if x > 0: #right move
            if self.la <= self.mra: #lep hit right end, singularity
                self.la = self.mra
                self.ra = self.mra
                self.lb = self.mrb
                self.rb = self.mrb
                self.lv = self.rv
            elif self.ra < self.mra: #rep exceeds right end compression
                diff = self.mra-self.ra
                self.rv -= diff
                self.ra = self.mra
                self.rb = self.mrb
        else: #left move
            if self.ra >= self.mla: #rep hit left end, singularity
                self.la = self.mla
                self.ra = self.mla
                self.lb = self.mlb
                self.rb = self.mlb
                self.rv = self.lv
            elif self.la > self.mla: #lep excceeds left end compression
                diff = self.la-self.mla
                self.lv += diff
                self.la = self.mla
                self.rb = self.mlb
        
    def eval(self,x,y):
        d = self.mla-x
        if d <= self.lv: return self.la
        elif d >= self.rv: return self.ra
        else: return self.la-d+self.lv

n,a,b = readints()
ar = readar()
states = list()
for i in range(a+b+1):
    states.append(zone(i,a,b))
for j in range(n):
    x = ar[j]
    for k in range(a+b+1):
        states[k].move(x)

#det answers here
for x in range(a+1):
    ans = list()
    for y in range(b+1):
        ans.append(states[x+y].eval(x,y))
    print(*ans)
