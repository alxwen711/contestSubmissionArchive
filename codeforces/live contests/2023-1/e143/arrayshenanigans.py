

def f(a):
    a.append(6)
ar = [1,2,3,4,5]
br = [1,2,3,4,5]
f(ar) #passes reference to the array
f(br[:3]) #indexing added, makes a copy of the array
print(ar)
print(br)
