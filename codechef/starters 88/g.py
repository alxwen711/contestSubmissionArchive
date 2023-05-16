import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
case of figuring out stuff like 10000000-1 = 1111111
initial zeros are copied to b c?
001111 = 010000 - 1

n 1's = 1 followed by n 0's - 1
3+ 1's always uses above
single 1 group should remain as such
2 1's either is fine? will not use above
first chain of 1's must be as is since b/c are len n strings

countercase: 011011011011 = 100000000000 - 000100100101 5 1's used
prev method has 8 1's used
cost of flip is 2 + 0 count
save potential is 1 count
010111 -> 100000 - 001001 -> 011000 - 000001
if chain of 2+ 0's, then can reset
almost 1 chain must have at least pos save potential, 1 count - 0 count > 2
01111001111 -> 10000000000 - 00000110001 or 10000010000 - 00001000001
"""
for i in range(readint()):
    n = readint()
    s = input()
    ar = [0]*n
    br = [0]*n
    zero = 0 # track if last digit in chain was 0
    zeros = list() # track zeros in chain
    chain = list() # track 1's in chain
    #st = -1
    index = 0
    while index < n:
        if s[index] == "1":
            ar[index] = 1
            index += 1
        else: break
    while index < n:
        x = s[index]
        if len(chain) == 0:
            if x == "1":
                chain = [index]
                zeros = list()
                zero = 0
                #st = index
        else:
            if x == "1":
                chain.append(index)
                zero = 0
            elif zero != 1:
                zero += 1
                zeros.append(index)
            else: # last two are zeros, remove
                zeros.pop()
                #zeros.pop() 2nd
                #zeros.pop() 3rd one was not recorded
                if (len(chain) - len(zeros)) >= 2: # can alt switch
                    ar[chain[0]-1] = 1
                    br[chain[-1]] = 1
                    for u in zeros:
                        br[u] = 1
                else: #fill in via chain
                    for k in chain:
                        ar[k] = 1

                chain = list()
                zeros = list()
        index += 1
    if len(chain) != 0: # possible end chain
        for snth in range(zero):
            zeros.pop()
        if (len(chain) - len(zeros)) >= 2: # can alt switch
            ar[chain[0]-1] = 1
            br[chain[-1]] = 1
            for uu in zeros:
                br[uu] = 1
        else: #fill in via chain
            for kk in chain:
                ar[kk] = 1

                
    print(*ar,sep="")
    print(*br,sep="")
    
