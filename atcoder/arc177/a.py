import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

a,b,c,d,e,f = readints()
n = readint()
ar = readar()
ans = "Yes"
for i in ar:
    x = i
    coins = min(f,x//500)
    f -= coins
    x -= coins*500
    coins = min(e,x//100)
    e -= coins
    x -= coins*100
    coins = min(d,x//50)
    d -= coins
    x -= coins*50
    coins = min(c,x//10)
    c -= coins
    x -= coins*10
    coins = min(b,x//5)
    b -= coins
    x -= coins*5
    coins = min(a,x)
    a -= coins
    x -= coins
    if x != 0:
        ans = "No"
        break
print(ans)
