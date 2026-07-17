import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
determine difference in AND/OR/XOR

use all 1's -> if it's AND, there will be no change for sure
use all 0's -> if it's OR or XOR, there will be no change for sure
if 0 used on AND, definitely going to change

first query can determine the type
if it's AND, then it should be possible to find in n+1 queries

otherwise if no change, 
"""

def solve(n):
    print(2**n-1)
    flush()
   
    print("I 0")
    flush()
    c1 = readint()

    print(f"I {2**n-1}")
    flush()
    c2 = readint()

    if c1 == 1 and c2 == 1: # must be OR with 2**n-1
        print(f"A 2 {2**n-1}")
        flush()
        return
    elif c1 == 1 and c2 == 2: # must be XOR with 2**n-1
        print(f"A 3 {2**n-1}")
        flush()
        return
    elif c1 == 2 and c2 == 2: # if 2**n-1, must be AND
        print("Q 1")
        flush()
        if readint() == 1: # must be 0 and 2**n-1
            print(f"A 1 {2**n-1}")
            flush()
            return
        else: # has to be OR with not 2**n-1, values in here are c and 2**n-1
            val = 0
            for ii in range(n-1,-1,-1):
                nv = val+(2**ii)
                print(f"Q {nv}")
                flush()
                if readint() == 2:
                    val = nv
            print(f"A 2 {val}")
            flush()
            return
    else: # follows 1 2 3 pattern, not 2**n-1, either AND or XOR
        print("Q 1")
        flush()
        if readint() == 3: # must be XOR
            val = 0
            for ii in range(n-2,-1,-1):
                nv = val+(2**ii)
                print(f"Q {nv}")
                flush()
                if readint() == 3:
                    val = nv
            val1 = val
            val2 = val ^ (2**n-1)
            # has to be either val1 or val2
            print(f"I {val1}")
            flush()
            if readint() == 4:
                print(f"A 3 {val1}")
                flush()
            else:
                print(f"A 3 {val2}")
                flush()
            return
        else: # must be AND
            val = 0
            for ii in range(n-1,-1,-1):
                nv = val+(2**ii)
                print(f"Q {nv}")
                flush()
                if readint() == 2:
                    val = nv
            print(f"A 1 {val}")
            flush()
            return



        
for _ in range(readint()):
    n = readint()
    if n == -1: break
    solve(n)






    
