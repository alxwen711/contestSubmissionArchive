#*ar to print all in ar sepearated by space
#moral of the story is that python hates keeping track of strings
import sys
for i in range(int(sys.stdin.readline())):
    n,k = map(int,sys.stdin.readline().split())
    o = k
    s = list(input())
    ar = [0]*n
    if k % 2 == 0: #keep 1
        for j in range(len(s)-1):
            if k == 0:
                break
            else:
                if s[j] == '0':
                    k -= 1
                    ar[j] = 1
                    s[j] = '1'
    else: #keep 0
        for j in range(len(s)-1):
            if k == 0:
                if s[j] == '0': s[j] = '1'
                else: s[j] = '0'
            else:
                if s[j] == '1':
                    k -= 1
                    ar[j] = 1
                s[j] = '1'
        
    ar[n-1] = k
    last = o-k
    if last % 2 == 1:
        if s[n-1] == '1': s[n-1] = '0'
        else: s[n-1] = '1'
    print(*s,sep='')
    print(*ar)
        
