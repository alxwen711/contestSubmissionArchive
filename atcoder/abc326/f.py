import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
two dp problems
even indicies up/down
odd indicies left/right

given co-ordinates, we should be able to determine what sum is needed
sumx//2+x//2 if even, use (x+1)//2 for odd case

need to find something faster than basic dp here
(worst case is effectively 10**9 or 2**40)

other idea would be trying highest to lowest values first
also removing the combinations that are for sure impossible
to reach target (remaining values do not have a high enough sum)
maybe this would be 2**20?
"""
n,x,y = readints()
ar = readar()
