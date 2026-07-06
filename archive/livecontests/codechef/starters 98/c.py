import sys
from math import gcd
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
not every setup is possible, could be off due to parity issues?
given x, gcd(n,x) cycles are considered
if n = 8, x = 6, then 0,2,4,6 and 1,3,5,7 are indiv problems
(even room never goes to an odd room here)
consider best setup with number of "moves" needed
if parity links, then good, else parity will be off by a move somewhere
so also consider best option with opposing parity

O(n^2)/O(m^2) ideas can work here
parity is just num of moves required
sum of a total setup of the parity should be 0 (mod n)
dp each element
with 1st one, find best with each parity
then add next element in w best parities from prev
at most m parity states
O(n*m*m)? unsure, could be optimized somehow
n,m <= 200, maybe doable
actually needs to be in a singular parity chain
"""

class problem: #container for problem info
    def __init__(self):
        self.rooms = 0
        self.students = list()
        self.stloc = list() #start location



for i in range(readint()):
    n,m,x = readints()
    ar = readar()
    br = list()
    for j in range(n):
        tmp = readar()
        br.append(tmp)
    # track student number to room
    room = list()
    for snth in range(m):
        room.append(list())
    for k in range(n):
        room[ar[k]-1].append(k) # 0 to n-1 index
    if x == 0: #no one can move, special case
        ans = 0
        for sn in range(n):
            ans += br[sn][ar[sn]-1]
        print(ans)
    else:
        g = gcd(m,x)
        gg = m//g
        if n == 0: print(0) #no students
        if n == 1: print(br[0][ar[0]-1]) #no change possible, 1 student
        else:
            parity = [-99999999999999999999999]*m #num of rooms for parity
            inc = 0
            while True:
                parity[inc] = br[0][(ar[0]+inc) % m]
                inc = (inc+x) % m
                if inc == 0: break
            for j in range(1,n): #iterate through each student
                np = [-99999999999999999999999]*m #next parities
                inc = 0
                while True: #k parity increment
                    v = br[j][(ar[j]+inc) % m] #value for k parity
                    for q in range(m):
                        cp = (q+inc) % m #combined parity
                        np[cp] = max(np[cp],parity[q]+v)
                    inc = (inc+x) % m
                    if inc == 0: break
                parity = np
            print(parity[0]) #best total with 0 parity        
