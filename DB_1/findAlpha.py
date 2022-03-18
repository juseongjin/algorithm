from sys import stdin
word = list(stdin.readline().strip())
stack = [-1]*26
cnt=0

for s in word:
    if stack[ord(s)-97] == -1:
        stack[ord(s)-97] = cnt
        cnt+=1
    else:
        cnt+=1
print(*stack)

# P.2
# word=list(stdin.readline().strip())
# stack=[-1]*26
# cnt=0
# for s in word:
#     stack[ord(s)-97]=word.index(s)
# print(*stack)
