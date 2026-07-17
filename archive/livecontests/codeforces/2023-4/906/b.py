import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
end game is 1 connecting with everything
(if 2 and 3 can connect, sum must be 6c or higher)
then one of the two must be connectable to 1
"""

for _ in range(readint()):
    n,c = readints()
    ar = readar()
    br = list()
    base = ar[0]
    for i in range(1,n):
        req = c*(i+1)-base-ar[i]
        br.append((req,i))
    attain = 0
    ans = "Yes"
    br.sort()
    for j in br:
        if j[0] > attain:
            ans = "No"
            break
        attain += ar[j[1]]
    print(ans)
