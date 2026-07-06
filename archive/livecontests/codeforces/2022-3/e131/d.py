import sys
for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ar = list(map(int,sys.stdin.readline().split()))
    low = [0]*n #track min value in this position
    high = [0]*n #track max value in this position
    for j in range(n):
        if ar[j] == 0:
            low[j] = j+2
            high[j] = n
        else:
            low[j] = ((j+1)//(ar[j]+1))+1
            high[j] = (j+1)//ar[j]
            if low[j] > high[j]: low[j] = high[j]

    """
    O(n^1.5?)
    create permutation by taking values with least options possible and
    giving them the value with least options remaining
    method below has cases with some positions being dead (no valid values remaining)
    
    """
    ans = [0]*n
    h = [0]*n #h[x] = how many places value x+1 could be placed in array 
    order = list()
    for k in range(n):
        tmp = list() #[# possible values, position, low, high]
        tmp.append(high[k]-low[k]+1)
        tmp.append(k)
        tmp.append(low[k])
        tmp.append(high[k])
        order.append(tmp)
        for m in range(low[k]-1,high[k]):
            h[m] += 1
    order.sort()
    for f in range(n):
        array = order[f]
        position = array[1]
        value = 99999999999
        lowest = 99999999999
        for g in range(array[2]-1,array[3]):
            if h[g] < lowest:
                lowest = h[g]
                value = g+1
            h[g] -= 1
        ans[position] = value
        h[value-1] = 99999999990 #taken
    print(*ans)
        
