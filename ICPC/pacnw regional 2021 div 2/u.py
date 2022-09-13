x = str(input())
y = x[::-1]
x *= 2
#print(y)
if x.count(y) != 0: print("1")
else: print("0")
