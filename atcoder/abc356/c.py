import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

# test all combinations

def generate(n,x):
    ans = [0]
    for i in range(n):
        ans.append(x % 2)
        x //= 2
    return ans

n,m,k = readints()
data = list()
for _ in range(m):
    br = list(map(str,sys.stdin.readline().split()))
    for i in range(len(br)-1):
        br[i] = int(br[i])
    data.append(br)
#print(data)
ans = 0
for a in range(2**n):
    ar = generate(n,a)
    #print(ar)
    flag = True
    for b in range(m):
        c = 0
        #print(data[b])
        for d in range(data[b][0]):
            c += ar[data[b][d+1]]
        #print(c)
        if data[b][-1] == "o":
            if c < k:
                flag = False
                break
        elif c >= k:
            flag = False
            break
    if flag:
        ans += 1
print(ans)
