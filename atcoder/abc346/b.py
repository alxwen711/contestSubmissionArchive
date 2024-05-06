import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

w,b = readints()
s = "wbwbwwbwbwbw"
n = len(s)
ss = s*((w+b+50)//n)
#print(ss)
ans = "No"
for i in range(len(ss)-w-b+1):
    x = ss[i:i+w+b]
    if x.count("w") == w and x.count("b") == b:
        ans = "Yes"
        break
print(ans)
