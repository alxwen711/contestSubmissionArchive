import sys

def find(a, val, b):
    low = val
    high = val
    j = 0
    while j < b:
        if a[j] >= low and a[j] <= high: return j
        elif a[j] > high:
            high = high*2+1
            low = low*2
        else: j += 1
    return -1

for x in range(int(sys.stdin.readline())):
    b = int(sys.stdin.readline())
    a = list(map(int,sys.stdin.readline().split()))
    a.sort()
    length = b
    possible = "YES"
    for i in range(b):
        index = find(a,b-i,length) #reverse order search
        if index == -1:
            possible = "NO"
            break
        else:
            a.pop(index)
            length += -1
    print(possible)
            
