ans = list()
for i in range(256):
    a = ""
    x = i
    for j in range(8):
        a = str(x%2) + a
        x = x//2
    ans.append(a)
print(ans)
        
