import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

a,b = map(str,input().split("|"))
s = input()
#print(a,b,s)
aa,bb,ss = len(a),len(b),len(s)
if (aa+bb+ss) % 2 == 1: print("Impossible")
elif ss < abs(aa-bb): print("Impossible")
else:
    diff = abs(aa-bb)
    seg = (ss-diff)//2
    sega,segb = s[diff:diff+seg],s[diff+seg:]
    if aa < bb: print(s[:diff] + sega + a + "|" + b + segb)
    else: print(sega + a + "|" + b + segb + s[:diff])
