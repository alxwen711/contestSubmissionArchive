import sys
oA = [[0,1,2,3],[1,2,3,0],[2,3,0,1],[3,0,1,2]]
oX = [[0,1,2,3],[1,0,3,2],[2,3,0,1],[3,2,1,0]]
for i in range(int(sys.stdin.readline())):
    #only the last two bits actually matter
    n, x, y = map(int,sys.stdin.readline().split(' '))
    ar = list(map(int,sys.stdin.readline().split(' ')))
    ans = x % 2
    for j in range(n):
        #ar[j] = ar[j] % 4
        if ar[j] % 2 == 1:
            ans += 1
    """a = x % 4
    b = (x+3) % 4
    """
    if ans % 2 == y % 2: print("Alice")
    else: print("Bob")
        
    
