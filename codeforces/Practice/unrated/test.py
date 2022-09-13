low = 1
high = 1000000
for i in range(20):
    mid = (low+high)//2
    print(mid, flush=True)
    react = str(input())
    if react == "<":
        high = mid
    else:
        low = mid
    if high-low == 1: break
    
print(high, flush=True)
react = str(input())
if react == "<": print("!",str(low))
else: print("!",str(high)) 
