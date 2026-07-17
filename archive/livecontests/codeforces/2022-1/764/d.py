import sys

for i in range(int(sys.stdin.readline())):
    #count pairs and singles in the string
    length,col = map(int,sys.stdin.readline().split())
    alpha = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    word = str(sys.stdin.readline())
    for j in range(length):
        alpha[ord(word[j])-97] += 1
    pairs = 0
    singles = 0
    answer = 0
    for k in range(26):
        pairs += (alpha[k]//2)
        singles += (alpha[k] % 2)
    answer = pairs//col
    singles += ((pairs-(answer*col))*2)
    answer = answer * 2
    if singles >= col: answer += 1
    print(answer)

